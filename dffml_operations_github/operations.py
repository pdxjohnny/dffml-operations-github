from typing import List

from dffml import op

from .api import GitHub, GitHubConfig


@op(
    imp_enter={"github": lambda self: GitHub(self.config)},
    ctx_enter={"gctx": lambda self: self.parent.github()},
    config_cls=GitHubConfig,
)
async def github_issues(self, url: str) -> List[dict]:
    return [
        issue
        async for issue in self.gctx.issues(
            *self.parent.github.owner_project(url)
        )
    ]


@op(
    imp_enter={"github": lambda self: GitHub(self.config)},
    ctx_enter={"gctx": lambda self: self.parent.github()},
    config_cls=GitHubConfig,
)
async def github_pull_requests(self, url: str) -> List[dict]:
    return [
        pull_request
        async for pull_request in self.gctx.pull_requests(
            *self.parent.github.owner_project(url)
        )
    ]
