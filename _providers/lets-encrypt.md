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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Lets Encrypt Agentic Access
  operation_count: 12
  slug: lets-encrypt-agentic-access
  summary_line: 12 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://acme-v02.api.letsencrypt.org
  baseurl_source: declared
  description: ACME account creation and management
  name: Let's Encrypt Account API
  slug: lets-encrypt-account-api
- baseURL: https://acme-v02.api.letsencrypt.org
  baseurl_source: declared
  description: Domain control authorizations
  name: Let's Encrypt Authorization API
  slug: lets-encrypt-authorization-api
- baseURL: https://acme-v02.api.letsencrypt.org
  baseurl_source: declared
  description: Issued certificate retrieval and revocation
  name: Let's Encrypt Certificate API
  slug: lets-encrypt-certificate-api
- baseURL: https://acme-v02.api.letsencrypt.org
  baseurl_source: declared
  description: Validation challenges (HTTP-01, DNS-01, TLS-ALPN-01)
  name: Let's Encrypt Challenge API
  slug: lets-encrypt-challenge-api
- baseURL: https://acme-v02.api.letsencrypt.org
  baseurl_source: declared
  description: Discovery document listing ACME resources
  name: Let's Encrypt Directory API
  slug: lets-encrypt-directory-api
- baseURL: https://acme-v02.api.letsencrypt.org
  baseurl_source: declared
  description: Anti-replay nonces for JWS-signed requests
  name: Let's Encrypt Nonce API
  slug: lets-encrypt-nonce-api
- baseURL: https://acme-v02.api.letsencrypt.org
  baseurl_source: declared
  description: Certificate issuance orders
  name: Let's Encrypt Order API
  slug: lets-encrypt-order-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Let's Encrypt ACME Account API
  slug: open-lets-encrypt-account-api
- collection_type: open
  name: Let's Encrypt ACME API
  slug: open-lets-encrypt-acme
- collection_type: open
  name: Let's Encrypt ACME Account Authorization API
  slug: open-lets-encrypt-authorization-api
- collection_type: open
  name: Let's Encrypt ACME Account Certificate API
  slug: open-lets-encrypt-certificate-api
- collection_type: open
  name: Let's Encrypt ACME Account Challenge API
  slug: open-lets-encrypt-challenge-api
- collection_type: open
  name: Let's Encrypt ACME Account Directory API
  slug: open-lets-encrypt-directory-api
- collection_type: open
  name: Let's Encrypt ACME Account Nonce API
  slug: open-lets-encrypt-nonce-api
- collection_type: open
  name: Let's Encrypt ACME Account Order API
  slug: open-lets-encrypt-order-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lets-encrypt-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lets-encrypt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lets-encrypt-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://letsencrypt.org/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/letsencrypt
- group: docs
  title: ''
  type: Specification
  url: https://datatracker.ietf.org/doc/html/rfc8555
- group: company
  title: ''
  type: Blog
  url: https://letsencrypt.org/feed.xml
created: '2026-03-16'
description: Let's Encrypt is a free, automated, and open certificate authority run by the Internet Security Research Group affiliated with the Linux Foundation. It provides TLS certificates to secure the web, having issued billions of certificates to enable HTTPS for websites worldwide via the ACME protocol.
finops:
- name: Lets Encrypt Finops
  service_category: API
  slug: lets-encrypt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lets-encrypt.png
layout: provider
modified: '2026-05-19'
name: Let's Encrypt
nav: Providers
network: true
overview: 'Let''s Encrypt publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Authorization API, Certificate API, and 4 more. Tagged areas include Certificates, Linux Foundation, Security, TLS, and ACME.


  Let''s Encrypt''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Lets Encrypt Plans Pricing
  plan_count: 3
  slug: lets-encrypt-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Lets Encrypt Rate Limits
  slug: lets-encrypt-rate-limits
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 45.4
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lets-encrypt/refs/heads/main/screenshots/lets-encrypt-2026-06-20T184427.png
security:
- kind: domain-security
  name: Lets Encrypt Domain Security
  slug: lets-encrypt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lets Encrypt Vulnerability Disclosure
  slug: lets-encrypt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lets-encrypt
tags:
- Certificates
- Linux Foundation
- Security
- TLS
- ACME
- PKI
---
