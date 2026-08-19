---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - sandbox
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Color''s partner-facing REST API — 13 operations over three surfaces: eligibility entries (list/create/read/update plus CSV or ANSI 834 file upload), population reporting (participants, samples, result'
  name: Color External API V1
  slug: color-eligibility-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/color-external-api-v1-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/color-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.color.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/color-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/color-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/color-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/color-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.color.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.color.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.color.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.color.com/docs/getting-started-with-color-apis
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.color.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://color.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/color
- group: start
  title: ''
  type: SignUp
  url: https://home.color.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://color.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://color.com/policies/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://color.com/policies/privacy
- group: company
  title: ''
  type: Website
  url: https://www.color.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/color-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/color-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/color-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/color-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/color-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/color-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/color-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/color-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/color-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/color-plans-pricing.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/color-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/color-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Color Health is an oncologist-led virtual cancer care company that provides screening, early detection, diagnosis, treatment guidance, and survivorship support to employers, health plans, unions, consultants, and public-sector organizations. Originally founded as a genomics testing company (Color Genomics), Color now operates a virtual clinical platform combining at-home testing kits, preventive health programs, and AI-assisted cancer care. For integration partners Color publishes an External API V1 at api.color.com/api/v1/external — 13 operations across eligibility entries, population reporting (participants, samples, results, self-reported results) and a lab/LIMS sample lifecycle — documented at docs.color.com/reference, alongside SAML-based SSO and SFTP/PGP file transfer for eligibility, claims, and member-event data.
image: https://www.color.com/wp-content/uploads/2021/02/Wordmark_Color_RGB.png
layout: provider
mcp_servers:
- description: ''
  name: color-mcp.yml
  slug: color-mcpyml
modified: '2026-08-15'
name: Color
nav: Providers
network: true
overview: 'Color publishes 1 API on the [APIs.io](https://apis.io/) network: External API V1. Tagged areas include Company, Health, Healthcare, Genomics, and Oncology.


  Color''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, signup flow, support, and 25 more developer resources.'
plans:
- name: Color Plans Pricing
  plan_count: 0
  slug: color-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 0
  name: Color Rate Limits
  slug: color-rate-limits
score:
  band: strong
  composite: 54.5
  delta: 1.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 30.3
    contract_quality: 59.9
    developer_ergonomics: 47.0
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 21.1
  previous_composite: 53.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/color/refs/heads/main/screenshots/color-2026-07-25T210056.png
security:
- kind: authentication
  name: Color Authentication
  slug: color-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Color Domain Security
  slug: color-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Color Vulnerability Disclosure
  slug: color-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Color Trust Center
  slug: color-trust-center
  summary_line: SOC 2, SOC 2 Type II, HIPAA, ISO 27001:2013, CSA STAR, CCPA, FISMA Moderate
slug: color
tags:
- Company
- Health
- Healthcare
- Genomics
- Oncology
- Cancer Care
- Preventive Health
- Eligibility
- Virtual Care
- Diagnostics
- Laboratory
- Employee Benefits
website: https://www.color.com
---
