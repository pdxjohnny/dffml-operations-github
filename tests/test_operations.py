import unittest

from dffml import AsyncTestCase, run_doctest

from dffml_operations_github.api import GitHubConfig
from dffml_operations_github.operations import (
    github_issues,
    github_pull_requests,
)

from .test_api import TOKEN


class TestOperations(AsyncTestCase):
    @unittest.skipUnless(TOKEN, "GitHub token required")
    async def test_github_issues(self):
        async with github_issues.imp(GitHubConfig(token=TOKEN)) as opimp:
            async with opimp(None, None) as ctx:
                issues = (
                    await ctx.run({"url": "https://github.com/intel/dffml"})
                )["result"]
                self.assertGreater(len(issues), 466)
                print(issues[0])

    @unittest.skipUnless(TOKEN, "GitHub token required")
    async def test_github_pull_requests(self):
        async with github_pull_requests.imp(
            GitHubConfig(token=TOKEN)
        ) as opimp:
            async with opimp(None, None) as ctx:
                pull_requests = (
                    await ctx.run({"url": "https://github.com/intel/dffml"})
                )["result"]
                self.assertGreater(len(pull_requests), 362)
                print(pull_requests[0])
