---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: MISP provides a RESTful API for threat sharing, documented at the official documentation site.
  name: MISP API
  slug: misp-api-2
- baseURL: https://github.com
  baseurl_source: declared
  description: The Agent Threat Rule API from MISP — 1 operation(s) for agent threat rule.
  name: MISP Agent Threat Rule API
  slug: misp-agent-threat-rule-api
artifact_total: 5
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/misp/refs/heads/main/rules/misp-rules.yml
  title: ''
  type: Spectral
  url: rules/misp-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/misp/refs/heads/main/conformance/misp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/misp-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/misp/refs/heads/main/well-known/misp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/misp-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/misp/refs/heads/main/well-known/misp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/misp-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/misp/refs/heads/main/hosts/misp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/misp-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/misp/refs/heads/main/vendors/misp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/misp-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.misp-project.org/support
- group: auth
  title: ''
  type: Security
  url: https://www.misp-project.org/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.misp-project.org/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MISP/
- group: docs
  title: ''
  type: Documentation
  url: https://www.misp-project.org/documentation/
- group: company
  title: ''
  type: Blog
  url: https://www.misp-project.org/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/misp/refs/heads/main/security/misp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/misp-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/misp/refs/heads/main/security/misp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/misp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.misp-project.org
coverage:
  checked: '2026-10-14'
  detail: Documentation exists but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://www.misp-project.org/documentation/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: MISP (Malware Information Sharing Platform & Threat Sharing) is an open source threat intelligence platform that enables sharing, storing and correlating of structured threat information. It provides a robust set of features including taxonomies, galaxy clusters, warning lists, and a flexible API for integration. The project is community‑driven and widely adopted by security teams, CERTs, and researchers worldwide to improve collaborative defense against cyber threats.
image: https://www.misp-project.org/img/sharing-default.png
layout: provider
modified: '2026-10-14'
name: MISP
nav: Providers
network: true
overview: 'MISP is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Agent Threat Rule API, and 1 more. Tagged areas include Open Source, ThreatIntelligence, Community, Security, and Collaboration.


  The MISP catalog on APIs.io includes 1 Spectral governance ruleset.


  MISP''s developer surface includes support, documentation, engineering blog, and 12 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: MISP API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: misp-rules
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 63.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Misp Domain Security
  slug: misp-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Misp Vulnerability Disclosure
  slug: misp-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: misp
tags:
- Open Source
- ThreatIntelligence
- Community
- Security
- Collaboration
- Company
website: https://www.misp-project.org
---
