---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: IDE plugins (VS Code, JetBrains, Vim, Emacs, Visual Studio, Sublime Text, etc.) surfacing autocomplete, chat, command, and Cascade-style agent edits backed by Codeium / Windsurf inference. There is no
  name: Codeium / Windsurf Plugins
  slug: plugins
- description: Enterprise / self-hosted SKU with admin dashboards, RBAC, analytics, and SSO. Sold as Windsurf Enterprise; legacy "Codeium for Enterprise" branding still appears in Windsurf navigation.
  name: Codeium for Enterprise (Windsurf Enterprise)
  slug: enterprise
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/codeium-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codeium-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Exafunction
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codeiumdev
- group: company
  title: ''
  type: Website
  url: https://windsurf.com/
- group: company
  title: ''
  type: LegacyWebsite
  url: https://codeium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.windsurf.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/codeium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/codeium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/codeium-finops.yml
created: '2026-05-08'
description: Codeium has been rebranded as Windsurf. The codeium.com URL now redirects to windsurf.com. The legacy Codeium product offered AI-powered code completion, search, and chat across IDEs (VS Code, JetBrains, Vim, Emacs, etc.). Codeium for Enterprise lives on as the enterprise / self-host SKU within Windsurf, alongside the Windsurf Editor and Plugins.
finops:
- name: Codeium Finops
  service_category: AI
  slug: codeium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codeium.png
layout: provider
modified: '2026-05-08'
name: Codeium
nav: Providers
network: true
overview: 'Codeium publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Developer Tools, Code Completion, IDE, and Windsurf.


  Codeium''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Codeium Plans Pricing
  plan_count: 1
  slug: codeium-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Codeium Rate Limits
  slug: codeium-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codeium/refs/heads/main/screenshots/codeium-2026-06-20T174702.png
security:
- kind: domain-security
  name: Codeium Domain Security
  slug: codeium-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Codeium Vulnerability Disclosure
  slug: codeium-vulnerability-disclosure
  summary_line: disclosure policy published
slug: codeium
tags:
- Artificial Intelligence
- Developer Tools
- Code Completion
- IDE
- Windsurf
- Rebranded
website: https://windsurf.com/
---
