---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.1
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: RESTful API (v2.0.0) for Arctic Wolf partner applications managing multiple customer tenants — create a partner application, generate an OAuth client-credentials bearer token, run health checks, and i
  name: Aurora Multi-Tenant API
  slug: aurora-multi-tenant-api
- description: RESTful API for organizations to manage Aurora Endpoint Security resources — Device API, User API, Global List API, Policy API, Zone API, Threat API, and Memory Protection API. Clients request an acce
  name: Aurora Endpoint Defense API
  slug: aurora-endpoint-defense-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: http://arcticwolf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.arcticwolf.com/en/developer-and-oem
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcticwolf.com/en
- group: docs
  title: ''
  type: APIReference
  url: https://docs.arcticwolf.com/bundle/aurora_mtc_api/page/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arcticwolf.com/en/developer-and-oem/aurora-multi-tenant-api/aurora-multi-tenant-api/getting-started
- group: company
  title: ''
  type: Blog
  url: https://arcticwolf.com/resources/blog/
- group: operate
  title: ''
  type: Support
  url: https://arcticwolf.com/company/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rtkwlf
- group: start
  title: ''
  type: SignUp
  url: https://arcticwolf.com/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcticwolf.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcticwolf.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/arctic-wolf-networks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/arctic-wolf-networks-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arctic-wolf-networks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.arcticwolf.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/arctic-wolf-networks-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arctic-wolf-networks-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arctic-wolf-networks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://arcticwolf.com/vulnerability-disclosure
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arctic-wolf-networks-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/arctic-wolf-networks-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arctic-wolf-networks-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arctic-wolf-networks-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arcticwolf.com/
created: '2026-07-17'
description: Arctic Wolf Networks is a security operations company delivering 24x7 AI-driven cybersecurity through its Aurora Platform, spanning Managed Detection and Response (MDR), Managed Risk, Managed Security Awareness, Incident Response, and Aurora Endpoint Security. For developers and OEM partners, Arctic Wolf publishes RESTful APIs on docs.arcticwolf.com — the Aurora Multi-Tenant API (2.0.0) for partners managing many customer tenants and the Aurora Endpoint Defense / User API for organizations managing devices, policies, zones, threats, and global lists. The APIs authenticate with an OAuth 2.0 client-credentials grant that mints a bearer access token. Arctic Wolf publishes a public trust center (SOC 2, ISO 27001/27017/27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR) and a coordinated vulnerability disclosure program via security.txt.
image: https://arcticwolf.com/wp-content/uploads/2026/03/AW-Higher-Standard-OG-Image-Dark-2026.jpg
layout: provider
modified: '2026-07-18'
name: Arctic Wolf Networks
nav: Providers
network: true
overview: 'Arctic Wolf Networks publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security Operations, Managed Detection and Response, and Endpoint Security.


  Arctic Wolf Networks'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 17 more developer resources.'
random_paper: 116
scopes:
- name: Arctic Wolf Networks Scopes
  scope_count: 1
  slug: arctic-wolf-networks-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 33.4
  delta: -0.2
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 33.6
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arctic-wolf-networks/refs/heads/main/screenshots/arctic-wolf-networks-2026-07-25T201104.png
security:
- kind: authentication
  name: Arctic Wolf Networks Authentication
  slug: arctic-wolf-networks-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Arctic Wolf Networks Domain Security
  slug: arctic-wolf-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arctic Wolf Networks Vulnerability Disclosure
  slug: arctic-wolf-networks-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Arctic Wolf Networks Trust Center
  slug: arctic-wolf-networks-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: arctic-wolf-networks
tags:
- Company
- Cybersecurity
- Security Operations
- Managed Detection and Response
- Endpoint Security
- Threat Detection
- Incident Response
website: http://arcticwolf.com/
---
