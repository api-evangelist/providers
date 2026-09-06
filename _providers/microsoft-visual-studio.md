---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.1
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The Visual Studio Extensibility API enables developers to create extensions that customize and extend Visual Studio IDE functionality. Extensions can add custom tool windows, commands, code analyzers,
  name: Visual Studio Extensibility API
  slug: extensibility-api
- description: The Visual Studio Marketplace API provides access to the extension marketplace for Visual Studio, VS Code, and Azure DevOps. Developers can search extensions, retrieve metadata, manage publisher profi
  name: Visual Studio Marketplace API
  slug: marketplace-api
- description: The VS Code Extension API enables developers to build extensions for Visual Studio Code. It provides APIs for language support, debugging, source control, terminal integration, webviews, custom editor
  name: VS Code Extension API
  slug: vscode-extension-api
artifact_total: 31
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-visual-studio-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-visual-studio
- group: start
  title: ''
  type: Portal
  url: https://marketplace.visualstudio.com/
- group: company
  title: ''
  type: Website
  url: https://visualstudio.microsoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/visualstudio/ide/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/vscode
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/microsoft/skills-for-copilot-studio
created: '2024-01-01'
description: Microsoft Visual Studio is an integrated development environment (IDE) for building applications. It provides APIs for extending the IDE functionality, publishing extensions to the marketplace, and building VS Code extensions.
finops:
- name: Microsoft Visual Studio Finops
  service_category: API
  slug: microsoft-visual-studio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-visual-studio.png
layout: provider
modified: '2026-05-19'
name: Microsoft Visual Studio
nav: Providers
network: true
overview: 'Microsoft Visual Studio publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Extensions, IDE, Microsoft, and VS Code.


  Microsoft Visual Studio''s developer surface includes developer portal, documentation, support, and 7 more developer resources.'
plans:
- name: Microsoft Visual Studio Plans Pricing
  plan_count: 3
  slug: microsoft-visual-studio-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Microsoft Visual Studio Rate Limits
  slug: microsoft-visual-studio-rate-limits
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-visual-studio/refs/heads/main/screenshots/microsoft-visual-studio-2026-06-20T185541.png
security:
- kind: domain-security
  name: Microsoft Visual Studio Domain Security
  slug: microsoft-visual-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 31
skills:
- name: add-action
  slug: add-action
- name: add-adaptive-card
  slug: add-adaptive-card
- name: add-generative-answers
  slug: add-generative-answers
- name: add-global-variable
  slug: add-global-variable
- name: add-knowledge
  slug: add-knowledge
- name: add-node
  slug: add-node
- name: add-other-agents
  slug: add-other-agents
- name: analyze-evals
  slug: analyze-evals
- name: chat-directline
  slug: chat-directline
- name: chat-sdk
  slug: chat-sdk
- name: chat-with-agent
  slug: chat-with-agent
- name: clone-agent
  slug: clone-agent
- name: create-eval-set
  slug: create-eval-set
- name: create-eval
  slug: create-eval
- name: detect-mode
  slug: detect-mode
- name: directline-chat
  slug: directline-chat
- name: edit-action
  slug: edit-action
- name: edit-agent
  slug: edit-agent
- name: edit-triggers
  slug: edit-triggers
- name: int-patterns
  slug: int-patterns
- name: int-project-context
  slug: int-project-context
- name: int-reference
  slug: int-reference
- name: list-kinds
  slug: list-kinds
- name: list-topics
  slug: list-topics
slug: microsoft-visual-studio
tags:
- Developer Tools
- Extensions
- IDE
- Microsoft
- VS Code
website: https://visualstudio.microsoft.com/
---
