from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class UpdatePerpMarketLpCooldownTimeArgs(typing.TypedDict):
    lp_cooldown_time: int


layout = borsh.CStruct("lp_cooldown_time" / borsh.I64)


class UpdatePerpMarketLpCooldownTimeAccounts(typing.TypedDict):
    admin: PublicKey
    state: PublicKey
    perp_market: PublicKey


def update_perp_market_lp_cooldown_time(
    args: UpdatePerpMarketLpCooldownTimeArgs,
    accounts: UpdatePerpMarketLpCooldownTimeAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["admin"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["state"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["perp_market"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x8d\xfb\x80\xf7XJ;\xdd"
    encoded_args = layout.build(
        {
            "lp_cooldown_time": args["lp_cooldown_time"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
