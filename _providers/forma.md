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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/forma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forma-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/forma-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.joinforma.com
- group: auth
  title: ''
  type: Security
  url: https://www.joinforma.com/legal/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.joinforma.com/platform/security
- group: auth
  title: ''
  type: Trust
  url: https://trust.joinforma.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joinforma.com/
- group: company
  title: ''
  type: Blog
  url: https://www.joinforma.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.joinforma.com/
- group: start
  title: ''
  type: Login
  url: https://client.joinforma.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinforma.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinforma.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/joinforma
created: '2026-07-17'
description: Forma is a flexible employee benefits platform, founded in 2017, that lets companies design, customize, and scale employee spending accounts from a single system. Employers select from a suite of Lifestyle Spending Accounts (LSA), Health Spending Accounts (HSA), Health Reimbursement Arrangements (HRA), and Flexible Spending Accounts (FSA), and employees access benefits through the Forma Store, the Forma Visa Card, or reimbursement claims. Forma connects to employer systems through 40+ HRIS and payroll integrations (Workday, ADP, UKG, Paylocity), SCIM provisioning, SAML2 SSO, and file feeds. Forma does not publish a public developer REST API; its technical surface is HRIS/SSO/SCIM integration and its trust posture (SOC 2 Type 2, HIPAA, GDPR). Backed by Emergence Capital, Ribbit Capital, and Uncork Capital.
image: https://cdn.prod.website-files.com/61fcf661d5fa0f6756473fea/62037846b95bd26645cb438c_Forma%20Logo%20Svg.svg
layout: provider
modified: '2026-07-19'
name: Forma
nav: Providers
network: true
overview: 'Forma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HR Tech, Employee Benefits, Lifestyle Spending Accounts, and Flexible Spending Accounts.


  Forma''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 18.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forma/refs/heads/main/screenshots/forma-2026-07-25T214946.png
security:
- kind: domain-security
  name: Forma Domain Security
  slug: forma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Forma Vulnerability Disclosure
  slug: forma-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Forma Trust Center
  slug: forma-trust-center
  summary_line: SOC 2 Type 2, HIPAA, GDPR
slug: forma
tags:
- Company
- HR Tech
- Employee Benefits
- Lifestyle Spending Accounts
- Flexible Spending Accounts
- Health Benefits
- HRIS Integration
- SCIM
website: https://www.joinforma.com
---
