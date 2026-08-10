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
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Vs Code Marketplace Agentic Access
  operation_count: 3
  slug: vs-code-marketplace-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 3
apis:
- description: Download extension assets including VSIX packages
  name: VS Code Marketplace Assets API
  slug: vs-code-marketplace-assets-api
- description: Query, search, and retrieve VS Code extensions from the Marketplace
  name: VS Code Marketplace Extensions API
  slug: vs-code-marketplace-extensions-api
- description: Publisher management and information
  name: VS Code Marketplace Publishers API
  slug: vs-code-marketplace-publishers-api
artifact_total: 16
collections:
- collection_type: open
  name: VS Code Marketplace Gallery API
  slug: open-vs-code-marketplace-gallery-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vs-code-marketplace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vs-code-marketplace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marketplace.visualstudio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://code.visualstudio.com/docs
- group: docs
  title: ''
  type: Guide
  url: https://code.visualstudio.com/api/working-with-extensions/publishing-extension
- group: start
  title: ''
  type: Portal
  url: https://marketplace.visualstudio.com/manage
- group: docs
  title: ''
  type: Documentation
  url: https://code.visualstudio.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://code.visualstudio.com/api/get-started/your-first-extension
- group: other
  title: ''
  type: Catalog
  url: https://marketplace.visualstudio.com/VSCode
- group: operate
  title: ''
  type: ChangeLog
  url: https://code.visualstudio.com/updates
- group: company
  title: ''
  type: Blog
  url: https://code.visualstudio.com/blogs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/microsoft/vscode
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/microsoft/vscode/issues
- group: operate
  title: ''
  type: Community
  url: https://code.visualstudio.com/community
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/visual-studio-code
- group: other
  title: ''
  type: X
  url: https://x.com/code
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-visual-studio-code
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@code
- group: commercial
  title: ''
  type: TermsOfService
  url: https://marketplace.visualstudio.com/policies/agree
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
created: '2024-01-01'
description: VS Code Marketplace is Microsoft's official extension marketplace for Visual Studio Code, offering thousands of extensions for languages, debuggers, themes, and developer tools. It provides a Gallery API for programmatically searching, discovering, and retrieving extension metadata, enabling integration with editors, tooling, and automation workflows.
examples:
- key_count: 5
  name: Vs Code Marketplace Downloadextension Example
  slug: vs-code-marketplace-downloadExtension-example
- key_count: 4
  name: Vs Code Marketplace Queryextensions Example
  slug: vs-code-marketplace-queryExtensions-example
finops:
- name: Vs Code Marketplace Finops
  service_category: API
  slug: vs-code-marketplace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vs-code-marketplace.png
json_schemas:
- name: VS Code Marketplace Extension
  property_count: 14
  slug: vs-code-marketplace-extension
json_structures:
- name: Vs Code Marketplace Extension Structure
  property_count: 0
  slug: vs-code-marketplace-extension-structure
jsonld:
- class_count: 0
  name: Vs Code Marketplace Context
  property_count: 8
  slug: vs-code-marketplace-context
layout: provider
modified: '2026-05-19'
name: VS Code Marketplace
nav: Providers
network: true
overview: 'VS Code Marketplace publishes 3 APIs on the [APIs.io](https://apis.io/) network: Assets API, Extensions API, and Publishers API. Tagged areas include Developer Tools, Extensions, IDE, and Microsoft.


  The VS Code Marketplace catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  VS Code Marketplace''s developer surface includes documentation, developer portal, getting-started guide, changelog, engineering blog, GitHub presence, Stack Overflow tag, and 13 more developer resources.'
plans:
- name: Vs Code Marketplace Plans Pricing
  plan_count: 3
  slug: vs-code-marketplace-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 5
  name: Vs Code Marketplace Rate Limits
  slug: vs-code-marketplace-rate-limits
rules:
- name: VS Code Marketplace API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vs-code-marketplace-jsonschema-spectral-rules
- name: VS Code Marketplace API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 4
  slug: vs-code-marketplace-rules
score:
  band: developing
  composite: 54.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.0
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vs-code-marketplace/refs/heads/main/screenshots/vs-code-marketplace-2026-06-20T201145.png
security:
- kind: domain-security
  name: Vs Code Marketplace Domain Security
  slug: vs-code-marketplace-domain-security
  summary_line: TLSv1.3
slug: vs-code-marketplace
tags:
- Developer Tools
- Extensions
- IDE
- Microsoft
website: https://marketplace.visualstudio.com/
---
