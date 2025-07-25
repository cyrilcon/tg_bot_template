from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import config


class AdminFilter(BaseFilter):
    """
    Filter for verifying the authenticity of the administrator.
    """

    is_admin: bool = True

    async def __call__(self, obj: Message) -> bool:
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin
