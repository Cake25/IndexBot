import datetime

from pony import orm

from plugins.index.utils.queue import update_approval_queue


@orm.db_session
def add_discord_server_to_queue(plugin, invite_code, server_id, server_name, server_description, invitee_id,
                                category_channel_name, genre_category_name):
    plugin.db.DiscordServer(state=1,
                            invite_code=invite_code,
                            server_id=server_id,
                            name=server_name,
                            description=server_description,
                            invitee_id=invitee_id,
                            submitted_at=datetime.datetime.now(),
                            category_channel_name=category_channel_name,
                            genre_category_name=genre_category_name,
                            # index_message_id=789,
                            last_checked=datetime.datetime.now())
    orm.commit()

    update_approval_queue(plugin)
    # TODO: logging logic


@orm.db_session
def remove_discord_server(plugin, discord_server):
    discord_server.delete()
    orm.commit()

    update_approval_queue(plugin)
    # TODO: index logic
    # TODO: logging logic


@orm.db_session
def update_discord_server(plugin, discord_server, attr=None):
    if attr is None:
        attr = {}

    discord_server.set(**attr)
    orm.commit()

    update_approval_queue(plugin)
    # TODO: index logic
    # TODO: logging logic
