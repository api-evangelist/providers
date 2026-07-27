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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Lets Encrypt Agentic Access
  operation_count: 12
  slug: lets-encrypt-agentic-access
  summary_line: 12 operations · 10 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: ACME account creation and management
  name: Let's Encrypt Account API
  slug: lets-encrypt-account-api
- description: Domain control authorizations
  name: Let's Encrypt Authorization API
  slug: lets-encrypt-authorization-api
- description: Issued certificate retrieval and revocation
  name: Let's Encrypt Certificate API
  slug: lets-encrypt-certificate-api
- description: Validation challenges (HTTP-01, DNS-01, TLS-ALPN-01)
  name: Let's Encrypt Challenge API
  slug: lets-encrypt-challenge-api
- description: Discovery document listing ACME resources
  name: Let's Encrypt Directory API
  slug: lets-encrypt-directory-api
- description: Anti-replay nonces for JWS-signed requests
  name: Let's Encrypt Nonce API
  slug: lets-encrypt-nonce-api
- description: Certificate issuance orders
  name: Let's Encrypt Order API
  slug: lets-encrypt-order-api
artifact_total: 14
collections:
- collection_type: open
  name: Let's Encrypt ACME API
  slug: open-lets-encrypt-acme
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
random_paper: 34
rate_limits:
- limit_count: 5
  name: Lets Encrypt Rate Limits
  slug: lets-encrypt-rate-limits
score:
  band: thin
  composite: 36.1
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 44.9
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 32.8
  schema_version: 0.5
  scored_at: '2026-07-27'
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
