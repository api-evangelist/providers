---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: start
  title: ''
  type: Signup
  url: https://developer.ubs.com/signup
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ubs-bank-usa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/ubs-bank-usa-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubs-bank-usa-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ubs-bank-usa-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ubs-bank-usa-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ubs-bank-usa-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ubs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ubs.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ubs.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://developer.ubs.com/support
- group: company
  title: ''
  type: Blog
  url: https://developer.ubs.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ubs
created: '2026-07-23'
description: UBS Bank USA (BUSA) is a Utah state-chartered industrial bank and FDIC-insured depository institution headquartered in Salt Lake City, Utah, established in 2003 and reporting roughly $122 billion in total assets. It is the primary US banking vehicle of UBS Wealth Management Americas, providing FDIC-insured deposit sweep programs, securities-based lending, mortgages, and credit cards almost exclusively to the high-net-worth and ultra-high-net-worth advisory clients of parent UBS Group AG. It is supervised by the FDIC, the Utah Department of Financial Institutions, and the CFPB. Unlike a fintech or a Banking-as-a-Service provider, UBS Bank USA exposes no first-party public developer API surface of its own; its services are delivered through UBS Financial Advisors rather than self-serve APIs. The only live UBS developer portal (developer.ubs.com) belongs to UBS Switzerland and serves Swiss and EU products (key4 mortgages, QR-bill, PSD2, TWINT, bLink, KeyPort/EBICS), not this US
  entity. US consumer-permissioned data access, where available, is mediated by third-party aggregators rather than a documented BUSA API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: UBS Bank USA
nav: Providers
network: true
overview: 'UBS Bank USA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Wealth Management, and Industrial Bank.


  UBS Bank USA''s developer surface includes signup flow, documentation, support, engineering blog, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.7
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Ubs Bank Usa Domain Security
  slug: ubs-bank-usa-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ubs Bank Usa Vulnerability Disclosure
  slug: ubs-bank-usa-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ubs-bank-usa
tags:
- Financial-Services
- Banking
- United States
- Wealth Management
- Industrial Bank
- Securities-Based Lending
- Private Banking
website: https://www.ubs.com
---
