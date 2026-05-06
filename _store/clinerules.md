---
aid: clinerules
name: .clinerules
url: https://raw.githubusercontent.com/api-evangelist/clinerules/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-27'
specificationVersion: '0.19'
type: Index
access: Public
position: Consumer
x-type: standard
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - Cline
  - Coding Standards
  - Configuration
  - Developer Workflow
  - Prompt Engineering
description: .clinerules is the rule-file convention used by the Cline open-source AI coding agent. Projects expose persistent guidance to Cline by placing a .clinerules/ directory at the repository root containing one or more Markdown or text files. Each file may declare optional YAML frontmatter to scope its instructions to glob patterns so the agent only loads context relevant to the active task. The format is interoperable with AGENTS.md, .cursorrules, and .windsurfrules conventions, providing a cross-tool standard for codifying coding conventions, architectural decisions, and behavioural constraints for AI coding agents.
apis: []
common:
  - type: Website
    url: https://cline.bot
  - type: Documentation
    url: https://docs.cline.bot/features/cline-rules
  - type: GitHubRepository
    url: https://github.com/cline/cline
  - type: JSONSchema
    url: json-schema/clinerules-rule-schema.json
  - type: JSONLDContext
    url: json-ld/clinerules-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
