---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 31
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering Agent Skills, the packaged, file-based capability units that AI coding agents load to extend their behavior. Agent Skills bundle instructions, scripts, schemas, and reference material into directories that agents discover, plan against, and execute at runtime, giving organizations a portable way to govern how AI assistants interact with their products and APIs. This collection tracks vendor-published skill repositories (Claude Code skills, Claude Agent SDK skills, Cursor rules, OpenAI Apps SDK skills, and capability packages) shipped by API providers across developer tools, data platforms, SaaS, and infrastructure.
examples:
- key_count: 14
  name: Agents Skills Skill Definition Example
  slug: agents-skills-skill-definition-example
- key_count: 10
  name: Agents Skills Skill Manifest Example
  slug: agents-skills-skill-manifest-example
features:
- description: Agent Skills bundle markdown instructions, executable scripts, schemas, and reference material into versioned directories that agents can load deterministically at runtime.
  name: File-Based Capability Packaging
- description: API providers ship official GitHub repositories such as resend-skills, ngrok/agent-skills, postman-skills, and jfrog-skills to deliver first-party automation behavior for their products.
  name: Vendor-Published Skill Repositories
- description: Skills surface a short SKILL.md frontmatter for discovery, then load deeper instructions, scripts, and assets only when an agent activates them, keeping token usage low.
  name: Progressive Disclosure of Context
- description: Skills package shell, Python, or Node scripts alongside instructions so agents can perform multi-step work (auth, file generation, API calls) instead of relying on prose-only prompting.
  name: Agent-Executable Tooling
- description: Skill formats are emerging across Claude Code, Claude Agent SDK, Cursor, OpenAI Apps SDK, and Gemini, with vendors publishing parallel skill sets for each runtime.
  name: Multi-Runtime Compatibility
- description: Organizations curate skill catalogs, sign skill manifests, and gate skill activation through allow lists so AI agents only run vetted capability packages.
  name: Skill Discovery and Governance
- description: Skills are increasingly generated from OpenAPI, AsyncAPI, and APIs.json descriptions so each API operation becomes a callable, governed capability inside an agent.
  name: API-First Skill Generation
- description: A growing ecosystem of community-maintained skill registries and indexes complements vendor repos, mirroring how the npm and PyPI ecosystems formed around packages.
  name: Open Skill Ecosystem
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Anthropic's official coding agent loads skills from the .claude/skills directory and surfaces them as plan-then-execute capabilities.
  name: Claude Code
- description: The Claude Agent SDK lets developers embed skill loading and execution into their own agent harnesses with the same SKILL.md contract as Claude Code.
  name: Claude Agent SDK
- description: Cursor consumes vendor rules and skill-style instruction bundles to extend its in-editor coding agent with provider-specific behavior.
  name: Cursor
- description: The OpenAI Apps SDK provides a skill-equivalent surface so apps and agents on the OpenAI platform can ship packaged capabilities to ChatGPT and developer tools.
  name: OpenAI Apps SDK
- description: Gemini's GEMINI.md and skill-style instruction files let vendors target Google's coding agent surface alongside Claude and Cursor.
  name: Google Gemini
- description: GitHub hosts the canonical distribution channel for skill repositories, including vendor-published agent-skills, claude-skills, and *-skills repos.
  name: GitHub
- description: Postman's skill repository ships first-party capabilities for working with Postman collections, workspaces, and the Postman API from coding agents.
  name: Postman
- description: Anthropic publishes the SKILL.md format, reference skill repositories, and the Skills feature in Claude Code that anchors the broader ecosystem.
  name: Anthropic
json_schemas:
- name: SkillDefinition
  property_count: 14
  slug: agents-skills-skill-definition
- name: SkillManifest
  property_count: 10
  slug: agents-skills-skill-manifest
json_structures:
- name: Agents Skills Skill Definition Structure
  property_count: 14
  slug: agents-skills-skill-definition-structure
- name: Agents Skills Skill Manifest Structure
  property_count: 10
  slug: agents-skills-skill-manifest-structure
jsonld:
- class_count: 9
  name: Agents Skills Context
  property_count: 19
  slug: agents-skills-context
layout: provider
modified: '2026-05-19'
name: Agent Skills
nav: Providers
network: true
overview: 'Agent Skills is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agent Skills, Claude Skills, Capability Packages, AI Agents, and Developer Tooling.


  The Agent Skills catalog on APIs.io includes 1 JSON-LD context.


  Agent Skills'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: agents-skills
tags:
- Agent Skills
- Claude Skills
- Capability Packages
- AI Agents
- Developer Tooling
use_cases:
- description: SaaS vendors ship official skill repos so AI agents in Claude Code or Cursor can create resources, run reports, and operate their products without bespoke prompt engineering.
  name: First-Party Product Skills
- description: Platform teams package their CI/CD, deployment, and observability workflows as governed skills so every engineering agent uses the same approved automations.
  name: Internal Developer Platform Skills
- description: API providers use skills to walk agents through authentication, sandbox setup, and "hello world" requests, accelerating time-to-first-call for developer-led agents.
  name: API Onboarding and Education
- description: Compliance-sensitive organizations distribute skills with allow-lists, signing, and audit trails to ensure only approved AI behaviors run against production systems.
  name: Governed Capability Distribution
- description: Teams convert OpenAPI specs into skill bundles (one operation per tool) so agents get typed, governed access to every endpoint without writing custom wrappers.
  name: API Specification to Skill Pipelines
- description: Vendors maintain mirror skill sets for Claude, Cursor, and OpenAI Apps SDK, giving customers a consistent experience across whichever coding agent they choose.
  name: Cross-Runtime Skill Portability
- description: Support and DevRel teams publish skills that diagnose common issues, pull logs, and open tickets, letting customer-side agents resolve problems autonomously.
  name: Skill-Driven Customer Support
- description: Skill bundles provision throwaway environments, seed test data, and tear down resources so agents can exercise APIs safely during development and CI.
  name: Sandbox and Test Environment Skills
website: https://apievangelist.com
---
