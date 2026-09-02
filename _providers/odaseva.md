---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 13.3
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/odaseva-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.odaseva.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.odaseva.com/security-trust
- group: auth
  title: ''
  type: Compliance
  url: https://www.odaseva.com/security-trust
- group: auth
  title: ''
  type: Security
  url: https://www.odaseva.com/responsibility-disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/odaseva-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/odaseva-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/odaseva-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/odaseva-well-known.yml
- group: company
  title: ''
  type: Blog
  url: https://www.odaseva.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.odaseva.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.odaseva.com/assets/pdf/Odaseva-Privacy-Policy.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.odaseva.com/assets/pdf/Odaseva-TermsofUse.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.odaseva.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/odaseva-lifecycle.yml
- group: build
  title: ''
  type: CLI
  url: cli/odaseva-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/odaseva-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/odaseva-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/odaseva-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/odaseva
- group: start
  title: ''
  type: Login
  url: https://platform.odaseva.com/CBR
coverage:
  checked: '2026-08-17'
  detail: Odaseva ships a real, versioned Platform API — the first-party odaseva-cli binary is a REST client for it and exposes an --apiVersion selector — but every path on its host api.odaseva.com answers a Salesforce My Domain 401 login challenge, and the reference that would describe it lives only in the customer knowledge base behind platform.odaseva.com/CBR; there is no developer subdomain at all (docs., developer., api-docs. and ten other candidates are NXDOMAIN) and the 376-URL sitemap contains no API, developer or documentation URL.
  evidence:
  - status: 401
    url: https://api.odaseva.com/openapi.json
  - status: 401
    url: https://api.odaseva.com/v1/openapi.json
  - status: 404
    url: https://www.odaseva.com/developers
  - status: 404
    url: https://www.odaseva.com/.well-known/agent-card.json
  - status: 404
    url: https://api.odaseva.com/mcp
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'Odaseva is an enterprise data security, backup, and governance platform purpose-built for large, complex Salesforce environments. It provides data backup and recovery, archiving, seeding and anonymization/masking, encryption and key management, privacy and data-residency controls, and data governance for regulated enterprises. Odaseva holds SOC 2 Type II, ISO 27001:2022, HITRUST, HIPAA, GDPR, CCPA, TISAX, IRAP, MLPS 2.0, and CSA STAR Level 2, with independent audits by Ernst & Young. Surfaced as a portfolio company of Partech and added to the API Evangelist network. Odaseva runs as a Salesforce-hosted application (api.odaseva.com and platform.odaseva.com are Salesforce My Domain hosts) and does have a versioned Odaseva Platform API, but it is customer-gated: every unauthenticated request returns a Salesforce login challenge and there is no public developer portal, OpenAPI, or reference. The one publicly installable client is the first-party Odaseva CLI on npm, last released
  2022-12-09; no server-side SDK is published on any registry. Odaseva runs an Atlassian Statuspage at trust.odaseva.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/odaseva.png
layout: provider
modified: '2026-08-17'
name: Odaseva
nav: Providers
network: true
overview: 'Odaseva is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure Saas, Salesforce, Data Protection, and Backup.


  Odaseva''s developer surface includes engineering blog, support, CLI, and 18 more developer resources.'
plans:
- name: Odaseva Plans Pricing
  plan_count: 0
  slug: odaseva-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Odaseva Rate Limits
  slug: odaseva-rate-limits
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 22.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/odaseva/refs/heads/main/screenshots/odaseva-2026-08-07T185947.png
security:
- kind: authentication
  name: Odaseva Authentication
  slug: odaseva-authentication
  summary_line: oauth2/password-login · 2 schemes
- kind: domain-security
  name: Odaseva Domain Security
  slug: odaseva-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Odaseva Vulnerability Disclosure
  slug: odaseva-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Odaseva Trust Center
  slug: odaseva-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, HITRUST, HIPAA, GDPR, CCPA, Privacy Shield, TISAX, IRAP, MLPS 2.0, CSA STAR Level 2
slug: odaseva
tags:
- Company
- Infrastructure Saas
- Salesforce
- Data Protection
- Backup
- Data Governance
- Security
- Compliance
- Privacy
website: https://www.odaseva.com/
---
