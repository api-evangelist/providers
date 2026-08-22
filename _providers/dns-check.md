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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dns Check Agentic Access
  operation_count: 1
  slug: dns-check-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: 'RESTful JSON API for managing DNS record monitors and DNS record group monitors at DNSCheck.co. All requests use GET and authenticate via a 32-character API key passed as the api_key query parameter; '
  name: DNS Check REST API
  slug: rest-api
- description: The DNS Record Monitoring API from DNS Check — 1 operation(s) for dns record monitoring.
  name: DNS Check DNS Record Monitoring API
  slug: dns-check-dns-record-monitoring-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DNS Check DNS Record Monitoring API
  slug: open-dns-check-dns-record-monitoring-api
- collection_type: open
  name: DNS Check API
  slug: open-dns-check
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dns-check-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dns-check-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dns-check-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dns-checker
- group: company
  title: ''
  type: Website
  url: https://www.dnscheck.co
- group: docs
  title: ''
  type: Documentation
  url: https://www.dnscheck.co/documentation
- group: docs
  title: ''
  type: API Documentation
  url: https://www.dnscheck.co/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dnscheck.co/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.dnscheck.co/signup
created: '2026-05-11'
description: DNS Check is a domain DNS monitoring service that lets teams monitor, share, and troubleshoot DNS records across multiple record types (A, AAAA, CNAME, MX, NS, PTR, SOA, SPF, SRV, TXT). The platform detects unresponsive name servers, incorrect IP addresses, missing or duplicated records, SPF record problems, and out-of-sync name servers, with notifications when records change or fail. The DNS Check REST API provides programmatic access to DNS record and DNS record group monitoring using a 32-character API key passed as a query parameter.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dns-check.png
layout: provider
modified: '2026-05-11'
name: DNS Check
nav: Providers
network: true
overview: 'DNS Check publishes 1 API on the [APIs.io](https://apis.io/) network: DNS Record Monitoring API. Tagged areas include DNS, DNS Monitoring, Domain Monitoring, DNS Records, and Infrastructure Monitoring.


  DNS Check''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 30.1
  delta: -0.3
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dns-check/refs/heads/main/screenshots/dns-check-2026-06-20T180058.png
security:
- kind: authentication
  name: Dns Check Authentication
  slug: dns-check-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dns Check Domain Security
  slug: dns-check-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dns-check
tags:
- DNS
- DNS Monitoring
- Domain Monitoring
- DNS Records
- Infrastructure Monitoring
- Networking
website: https://www.dnscheck.co
---
