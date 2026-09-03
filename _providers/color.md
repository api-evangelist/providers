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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://api.color.com/api/v1/external
  baseurl_source: declared
  description: Eligibility entries and eligibility-file uploads for a population.
  name: Color Eligibility API
  slug: color-eligibility-api
- baseURL: https://api.color.com/api/v1/external
  baseurl_source: declared
  description: 'Read-side queries across a population: participants, results, samples, self-reported results.'
  name: Color Populations API
  slug: color-populations-api
- baseURL: https://api.color.com/api/v1/external
  baseurl_source: declared
  description: 'Lab/LIMS sample lifecycle: accession, result reporting, destruction.'
  name: Color Samples API
  slug: color-samples-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/color-capability-edges.yml
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
  name: Color MCP Server
  slug: color-mcp-server
modified: '2026-08-15'
name: Color
nav: Providers
network: true
overview: 'Color publishes 3 APIs on the [APIs.io](https://apis.io/) network: Eligibility API, Populations API, and Samples API. Tagged areas include Company, Health, Healthcare, Genomics, and Oncology.


  Color''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, signup flow, support, and 26 more developer resources.'
plans:
- name: Color Plans Pricing
  plan_count: 0
  slug: color-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Color Rate Limits
  slug: color-rate-limits
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 51.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
