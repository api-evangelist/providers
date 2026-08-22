---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 20
  human_in_the_loop: 2
  name: Codesandbox Agentic Access
  operation_count: 27
  slug: codesandbox-agentic-access
  summary_line: 27 operations · 20 acting · 2 human-in-the-loop
api_count: 10
apis:
- description: The Define API allows programmatic creation of browser sandboxes from code files, useful for documentation sites and code examples that need to generate a sandbox on the fly. Supports both GET and POS
  name: CodeSandbox Define API
  slug: define-api
- description: Sandpack is an open-source component toolkit for creating live-running code editing experiences powered by CodeSandbox. It supports React via @codesandbox/sandpack-react and plain JavaScript via @code
  name: Sandpack Embed Toolkit
  slug: sandpack
- description: API metadata and auth context
  name: CodeSandbox meta API
  slug: codesandbox-meta-api
- description: Trusted preview host management
  name: CodeSandbox preview_host API
  slug: codesandbox-preview-host-api
- description: Preview token management for private sandboxes
  name: CodeSandbox preview_token API
  slug: codesandbox-preview-token-api
- description: Browser and VM sandbox management
  name: CodeSandbox sandbox API
  slug: codesandbox-sandbox-api
- description: Sandbox template management
  name: CodeSandbox templates API
  slug: codesandbox-templates-api
- description: API token management
  name: CodeSandbox token API
  slug: codesandbox-token-api
- description: Virtual machine lifecycle management
  name: CodeSandbox vm API
  slug: codesandbox-vm-api
- description: Workspace and organization management
  name: CodeSandbox workspace API
  slug: codesandbox-workspace-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CodeSandbox meta API
  slug: open-codesandbox-meta-api
- collection_type: open
  name: CodeSandbox meta sandbox API
  slug: open-codesandbox-sandbox-api
- collection_type: open
  name: CodeSandbox meta templates API
  slug: open-codesandbox-templates-api
- collection_type: open
  name: CodeSandbox meta token API
  slug: open-codesandbox-token-api
- collection_type: open
  name: CodeSandbox meta vm API
  slug: open-codesandbox-vm-api
- collection_type: open
  name: CodeSandbox meta workspace API
  slug: open-codesandbox-workspace-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/codesandbox/sandpack/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/codesandbox/sandpack/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/codesandbox/sandpack/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/codesandbox/sandpack/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codesandbox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codesandbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codesandbox-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://codesandbox.io
- group: docs
  title: ''
  type: Documentation
  url: https://codesandbox.io/docs/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codesandbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codesandbox
- group: other
  title: ''
  type: X
  url: https://x.com/codesandbox
- group: company
  title: ''
  type: Blog
  url: https://codesandbox.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://codesandbox.io/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://codesandbox.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codesandbox.io
- group: commercial
  title: ''
  type: Plans
  url: plans/codesandbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/codesandbox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/codesandbox-finops.yml
created: '2026-06-12'
description: CodeSandbox is a browser-based development environment platform that enables developers to create, share, and collaborate on interactive coding sandboxes instantly in the browser. The platform provides a cloud-based IDE with Firecracker microVM infrastructure that supports snapshotting, cloning, and running isolated development environments at scale. CodeSandbox offers the CodeSandbox SDK for programmatically spinning up AI sandboxes and development environments, the Sandpack component toolkit for embedding live-running code editing experiences, and a browser sandbox Define API for generating sandboxes on the fly from code examples. Trusted by over 4.5 million developers monthly, it serves individual developers, professional teams, and AI product builders needing concurrent sandboxed environments.
examples:
- key_count: 4
  name: Codesandbox Sandbox Create Example
  slug: codesandbox-sandbox-create-example
- key_count: 4
  name: Codesandbox Sandbox List Example
  slug: codesandbox-sandbox-list-example
- key_count: 4
  name: Codesandbox Vm Create Session Example
  slug: codesandbox-vm-create-session-example
- key_count: 4
  name: Codesandbox Vm Start Example
  slug: codesandbox-vm-start-example
finops:
- name: Codesandbox Finops
  service_category: Developer Tools
  slug: codesandbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codesandbox.png
json_schemas:
- name: MetaInformation
  property_count: 3
  slug: codesandbox-meta-information
- name: PreviewToken
  property_count: 4
  slug: codesandbox-preview-token
- name: Sandbox
  property_count: 9
  slug: codesandbox-sandbox
- name: VMStartResponse
  property_count: 3
  slug: codesandbox-vm-start-response
jsonld:
- class_count: 0
  name: Codesandbox Context
  property_count: 46
  slug: codesandbox-context
layout: provider
modified: '2026-06-12'
name: CodeSandbox
nav: Providers
network: true
overview: 'CodeSandbox publishes 8 APIs on the [APIs.io](https://apis.io/) network, including meta API, preview_host API, preview_token API, and 5 more. Tagged areas include Developer Tools, Cloud IDE, Code Sandboxes, Browser Development, and AI Sandboxes.


  The CodeSandbox catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CodeSandbox''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, and 14 more developer resources.'
plans:
- name: Codesandbox Plans Pricing
  plan_count: 4
  slug: codesandbox-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 7
  name: Codesandbox Rate Limits
  slug: codesandbox-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CodeSandbox API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: codesandbox-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.1
  delta: -8.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 68.9
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 50.0
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/codesandbox/refs/heads/main/screenshots/codesandbox-2026-06-20T174706.png
security:
- kind: authentication
  name: Codesandbox Authentication
  slug: codesandbox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Codesandbox Domain Security
  slug: codesandbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codesandbox
tags:
- Developer Tools
- Cloud IDE
- Code Sandboxes
- Browser Development
- AI Sandboxes
- Code Embedding
website: https://codesandbox.io
---
