---
aid: copilot-instructions-md
url: https://raw.githubusercontent.com/api-evangelist/copilot-instructions-md/refs/heads/main/apis.yml
name: copilot-instructions.md
x-type: standard
description: copilot-instructions.md is a GitHub Copilot custom instructions file placed at .github/copilot-instructions.md in a repository. It provides repository-specific guidance and preferences that GitHub Copilot Chat, Copilot in the IDE, and the Copilot coding agent automatically inject into prompts when working in the repository. The file is plain Markdown in natural language, helping the AI understand build, test, validation, framework, and style conventions so it can produce code that is consistent with the project's expectations and reduce pull request rejections caused by avoidable lint, CI, or convention failures.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Coding
  - Coding Standards
  - Copilot
  - Custom Instructions
  - Developer Workflow
  - GitHub
  - GitHub Copilot
  - Markdown
  - Repository
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: copilot-instructions-md:format
    name: copilot-instructions.md Format
    tags:
      - Convention
      - GitHub Copilot
      - Markdown
      - Repository
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
    properties:
      - url: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
        type: Documentation
      - url: https://github.blog/changelog/2025-01-23-custom-instructions-for-github-copilot-in-vs-code-now-generally-available/
        type: Blog
      - url: https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses
        type: Documentation
      - url: https://github.com/github/awesome-copilot
        type: Examples
    description: The copilot-instructions.md format is an unstructured Markdown file placed at .github/copilot-instructions.md. GitHub Copilot detects the file automatically and prepends its contents to prompts sent to the model in Copilot Chat, Copilot in the IDE, and the Copilot coding agent. The file accepts free-form natural language instructions, with whitespace between sections ignored, and is rendered as a reference in Copilot Chat replies so users can confirm it was consulted.
    x-features:
      - Auto-loaded by GitHub Copilot Chat, IDE plugins, and coding agent
      - Resides at the canonical path .github/copilot-instructions.md
      - Plain Markdown - no required schema or front matter
      - Visible reference in Copilot Chat replies that consume the file
      - Pairs with .github prompt files and Copilot agent rulesets
      - Effective immediately upon save; no Copilot configuration step
    x-useCases:
      - Telling Copilot which test runner, linter, and build commands to use
      - Steering Copilot to preferred libraries or framework patterns
      - Communicating commit message and branch naming conventions
      - Documenting code style, naming, and comment conventions
      - Reducing CI failures caused by Copilot generated code
  - aid: copilot-instructions-md:related-conventions
    name: Copilot Instructions Ecosystem
    tags:
      - AI Coding
      - Conventions
      - GitHub Copilot
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.github.com/en/copilot/customizing-copilot
    properties:
      - url: https://docs.github.com/en/copilot/customizing-copilot
        type: Documentation
      - url: https://docs.github.com/en/copilot/customizing-copilot/adding-personal-custom-instructions-for-github-copilot
        type: Documentation
      - url: https://docs.github.com/en/copilot/customizing-copilot/adding-organization-custom-instructions-for-github-copilot
        type: Documentation
      - url: https://docs.github.com/en/copilot/customizing-copilot/adding-prompt-files-to-your-repository
        type: Documentation
    description: Repository copilot-instructions.md is one layer in a stack of GitHub Copilot customization options. Personal custom instructions apply to a single user across all repositories. Organization custom instructions apply to every repository in a GitHub organization. Path-scoped .github/instructions/*.instructions.md files target specific files or globs. Prompt files in .github/prompts/ provide reusable named prompts. The copilot-instructions.md file sits at the repository tier and travels with the code, providing the same context to every collaborator.
    x-features:
      - Composes with personal and organization-level instructions
      - Path-scoped .instructions.md files override repo-wide instructions
      - Reusable prompts in .github/prompts/*.prompt.md
      - Effective in Copilot Chat, Copilot in IDE, and Copilot coding agent
      - Versioned and reviewed alongside code through pull requests
    x-useCases:
      - Applying organization-wide guardrails across all repos
      - Layering repo-specific rules on top of organization defaults
      - Targeting language-specific conventions to subdirectories
      - Sharing reusable named prompts with all collaborators
common:
  - type: Documentation
    url: https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
  - type: Documentation
    url: https://docs.github.com/en/copilot/customizing-copilot
  - type: Examples
    url: https://github.com/github/awesome-copilot
  - type: Blog
    url: https://github.blog/changelog/2025-01-23-custom-instructions-for-github-copilot-in-vs-code-now-generally-available/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
