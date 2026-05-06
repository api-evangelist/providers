---
aid: agents-md
name: AGENTS.md
description: AGENTS.md is an open standard file format that provides context and instructions to AI coding agents working on software projects. Like a README for agents, an AGENTS.md file lives in the project repository and tells AI agents how to build, test, and contribute code — including coding standards, build commands, testing procedures, and development conventions. Supported by over 60,000 open-source projects and major platforms including OpenAI Codex, Google Jules, Cursor, Devin, Windsurf, GitHub Copilot, and goose. Stewarded by the Agentic AI Foundation under the Linux Foundation.
url: https://raw.githubusercontent.com/api-evangelist/agents-md/refs/heads/main/apis.yml
humanURL: https://agents.md/
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - AI Copilot
  - Coding Standards
  - Developer Workflow
  - Open Standard
  - Documentation
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: agents-md:agents-md-specification
    name: AGENTS.md Specification
    description: The AGENTS.md specification defines a standard Markdown file format for providing project context, build instructions, coding standards, and testing procedures to AI coding agents. The file is version-controlled with the project and discovered by AI tools at predictable locations in the repository tree.
    humanURL: https://agents.md/
    tags:
      - Open Standard
      - AI Agents
      - Developer Workflow
      - Specification
    properties:
      - type: Documentation
        url: https://agents.md/
      - type: GitHubRepository
        url: https://github.com/openai/agents.md
common:
  - type: Portal
    url: https://agents.md/
  - type: Documentation
    url: https://agents.md/
  - type: GitHubOrganization
    url: https://github.com/agentic-ai-foundation
  - type: Features
    data:
      - name: Project Context for AI Agents
        description: Provides AI agents with structured information about the project including its purpose, architecture, and key concepts.
      - name: Build and Test Instructions
        description: Documents the exact commands needed to build, test, lint, and deploy the project so AI agents can execute them correctly.
      - name: Coding Standards
        description: Specifies coding conventions, style guides, naming patterns, and best practices that AI agents should follow when generating code.
      - name: Monorepo Support
        description: Supports nested AGENTS.md files in monorepo subdirectories, allowing different projects to have tailored agent instructions with closest-file-wins precedence.
      - name: Open Standard with No Required Fields
        description: The format uses standard Markdown with no mandatory fields, giving teams flexibility to include only the context their agents need.
      - name: Broad Tool Support
        description: Supported by 60+ AI coding tools and editors including OpenAI Codex, Google Jules, Cursor, Devin, GitHub Copilot, Windsurf, and goose.
  - type: UseCases
    data:
      - name: AI-Assisted Code Review
        description: Provide AI coding agents with project conventions and standards so their generated code passes review without needing manual style corrections.
      - name: Autonomous Feature Development
        description: Enable AI agents to independently implement features by giving them the context needed to set up the development environment, run tests, and validate their work.
      - name: Onboarding AI Agents to Existing Projects
        description: Accelerate AI agent productivity on legacy codebases by documenting the context that would normally come from exploring the project.
      - name: Consistent Multi-Agent Workflows
        description: Ensure all AI agents working on a project operate from the same context, reducing inconsistencies when multiple agents collaborate.
      - name: Security-Aware AI Development
        description: Document security considerations and sensitive file locations so AI agents avoid introducing vulnerabilities or accidentally exposing credentials.
  - type: Integrations
    data:
      - name: OpenAI Codex
        description: Native AGENTS.md support for AI coding tasks via OpenAI's coding agent.
      - name: Google Jules
        description: AGENTS.md context ingestion in Google's AI coding agent for autonomous development tasks.
      - name: Cursor
        description: AGENTS.md file discovery and context loading in Cursor's AI-assisted editor.
      - name: Devin (Cognition)
        description: AGENTS.md support in Cognition's autonomous coding agent Devin.
      - name: GitHub Copilot
        description: AGENTS.md integration in GitHub Copilot for project-aware AI code suggestions.
      - name: goose (AAIF)
        description: AGENTS.md context loading in Block's open-source goose AI agent, now under the Agentic AI Foundation.
      - name: Windsurf
        description: AGENTS.md support in Windsurf's AI-powered development environment.
      - name: JetBrains Junie
        description: AGENTS.md discovery in JetBrains' AI coding assistant Junie.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
