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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://raven.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.raven.io
- group: company
  title: ''
  type: Blog
  url: https://raven.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://raven.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://raven.io/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://raven.io/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/raven-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/raven-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raven-domain-security.yml
created: '2026-07-17'
description: Raven is a runtime security platform that protects applications from the inside, detecting and preventing malicious code execution as it happens rather than relying only on perimeter defenses. Its capabilities span Runtime Prevention (blocking exploit execution regardless of CVE availability), Runtime ADR (application-level attack detection and response with forensics), Runtime AI-Agents (discovering and monitoring AI agents in an environment), Runtime SCA (prioritizing vulnerable dependencies by actual execution), and Runtime Gatekeeper (keeping risky applications out of production). The platform is self-hosted on Kubernetes, deployed via Helm/OCI charts and a sensor operator across AWS, Azure, and GCP, and is positioned as an application-level alternative to WAF, EDR, RASP, SCA, and ASPM tools. Raven is a portfolio company of Norwest Venture Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raven.png
layout: provider
modified: '2026-07-20'
name: Raven
nav: Providers
network: true
overview: 'Raven is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Application Security, Runtime Security, and Cybersecurity.


  Raven''s developer surface includes documentation, engineering blog, pricing, and 6 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/raven/refs/heads/main/screenshots/raven-2026-09-02T152922.png
security:
- kind: domain-security
  name: Raven Domain Security
  slug: raven-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: raven
tags:
- Company
- Security
- Application Security
- Runtime Security
- Cybersecurity
- Cloud Security
- Kubernetes
- Vulnerability Management
website: https://raven.io
---
