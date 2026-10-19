"""Harbor agent: Pi coding agent running under the DRIFT defense extension.

Usage:
    harbor run -p harbor_drift/tasks/<task> \
        -a harbor_drift.pi_drift.agent:DriftPi \
        -m zai-coding-cn/glm-5.3-flash --ae ZAI_CODING_CN_API_KEY=$GLM_API_KEY
"""

import shlex
from pathlib import Path

from harbor.agents.installed.pi import _REMOTE_PI_CONFIG_DIR, Pi
from harbor.environments.base import BaseEnvironment
from harbor.models.agent.context import AgentContext

_EXTENSION_SOURCE = Path(__file__).with_name("drift.ts")
_REMOTE_EXTENSION = _REMOTE_PI_CONFIG_DIR / "drift.ts"


class DriftPi(Pi):
    @staticmethod
    def name() -> str:
        return "pi-drift"

    def build_cli_flags(self) -> str:
        flags = super().build_cli_flags()
        return f"{flags} --extension {shlex.quote(_REMOTE_EXTENSION.as_posix())}".strip()

    async def run(
        self,
        instruction: str,
        environment: BaseEnvironment,
        context: AgentContext,
    ) -> None:
        await self._ensure_config_dir(environment)
        await self._upload_config_text(
            environment,
            content=_EXTENSION_SOURCE.read_text(),
            remote_path=_REMOTE_EXTENSION.as_posix(),
            filename="drift.ts",
        )
        await super().run(instruction, environment, context)
