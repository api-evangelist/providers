---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-09-14'
api_count: 1
apis:
- description: ACORD 25 Data Extraction & COI Verification. Extract a certificate of insurance into structured fields and verify it against saved coverage requirements, with a three-state verdict (compliant / defici
  name: Aervik Labs API
  slug: aervik-labs-api
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aervik-labs/refs/heads/main/security/aervik-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aervik-labs-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aervik-labs/refs/heads/main/authentication/aervik-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aervik-labs-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aervik-labs/refs/heads/main/security/aervik-labs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aervik-labs-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aervik-labs/refs/heads/main/security/aervik-labs-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aervik-labs-vulnerability-disclosure.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aervik-labs/refs/heads/main/packages/aervik-labs-packages.yml
  title: ''
  type: Packages
  url: packages/aervik-labs-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aervik-labs/refs/heads/main/llms/aervik-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aervik-labs-llms.txt
- group: company
  title: ''
  type: Website
  url: https://aerviklabs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aerviklabs.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://aerviklabs.com/apis/coi-verification/
- group: company
  title: ''
  type: Blog
  url: https://aerviklabs.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aervik-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://aerviklabs.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://rapidapi.com/aervik-labs-aervik-labs-default/api/certificate-of-insurance-verification-compliance-check-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aerviklabs.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aerviklabs.com/privacy/
created: '2026-09-14'
description: Aervik Labs is a narrow, well-documented API operated by EAC Ventures, LLC that extracts and verifies ACORD 25 Certificates of Insurance (COI) against your own coverage requirements. It parses a certificate into structured fields, checks it for compliance, and returns a three-state verdict that tells contractors, property managers and risk teams plainly when a value is deficient versus when it simply could not be read. Distributed through the RapidAPI marketplace with a free evaluation tier.
image: https://aerviklabs.com/images/aervik-labs-logo-primary.png
layout: provider
mcp_servers:
- description: ''
  name: Aervik Labs MCP Server
  slug: aervik-labs-mcp-server
modified: '2026-09-14'
name: Aervik Labs
nav: Providers
network: true
overview: 'Aervik Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Compliance, Verification, Insurtech, and Certificate of Insurance.


  Aervik Labs'' developer surface includes authentication, API reference, engineering blog, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Aervik Labs Plans Pricing
  plan_count: 4
  slug: aervik-labs-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Aervik Labs Rate Limits
  slug: aervik-labs-rate-limits
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 47.0
    discoverability: 75.9
    operational_transparency: 71.1
  provenance:
    conformance: derived
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
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aervik Labs Authentication
  slug: aervik-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aervik Labs Domain Security
  slug: aervik-labs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aervik Labs Vulnerability Disclosure
  slug: aervik-labs-vulnerability-disclosure
  summary_line: disclosure policy published
slug: aervik-labs
tags:
- Insurance
- Compliance
- Verification
- Insurtech
- Certificate of Insurance
- ACORD 25
- Document Intelligence
- RapidAPI
website: https://aerviklabs.com
---
