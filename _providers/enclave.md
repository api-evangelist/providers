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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enclave-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://enclave.ai/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enclave-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/enclave-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/enclave-security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.enclave.ai
- group: company
  title: ''
  type: Blog
  url: https://enclave.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://enclave.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enclave.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enclave.ai/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://enclave.ai
created: '2026-07-17'
description: Enclave (enclave.ai) is an AI-powered application and cloud security platform that operates as an "agentic security engineer." It continuously builds a living model of an organization's attack surface across services and cloud providers, then autonomously triages and investigates vulnerability findings against known CVEs to determine real-world exploitability and reachability. Rather than flooding teams with signature-based noise, Enclave traces data flows to confirm whether a CVE is actually reachable, surfaces cross-service exploits that traditional scanners miss, and routes prioritized remediation plans with proof to the owning teams. Founded by veterans from Stripe, Box, VMware, Salesforce, and Yelp, the company is backed by 8VC and Marc Benioff. Added to the API Evangelist network and enriched from the company's public web surface; no public developer API is currently published.
image: https://enclave.ai/img/redesign/footer/logo-wordmark.svg
layout: provider
modified: '2026-07-19'
name: Enclave
nav: Providers
network: true
overview: 'Enclave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Application Security, Cloud Security, and Vulnerability Management.


  Enclave''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enclave/refs/heads/main/screenshots/enclave-2026-07-25T213259.png
security:
- kind: domain-security
  name: Enclave Domain Security
  slug: enclave-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Enclave Vulnerability Disclosure
  slug: enclave-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: enclave
tags:
- Company
- Security
- Application Security
- Cloud Security
- Vulnerability Management
- Artificial Intelligence
- Agentic AI
- CVE
- DevSecOps
website: https://enclave.ai
---
