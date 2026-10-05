---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.apiiro.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiiroltd/refs/heads/main/security/apiiroltd-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/apiiroltd-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiiroltd/refs/heads/main/llms/apiiroltd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiiroltd-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiiroltd/refs/heads/main/well-known/apiiroltd-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apiiroltd-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiiroltd/refs/heads/main/well-known/apiiroltd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apiiroltd-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiiroltd/refs/heads/main/hosts/apiiroltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiiroltd-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiiroltd/refs/heads/main/vendors/apiiroltd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apiiroltd-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.apiiro.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apiiro.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiiro.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiiro
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiiroltd/refs/heads/main/security/apiiroltd-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/apiiroltd-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiiroltd/refs/heads/main/security/apiiroltd-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apiiroltd-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiiroltd/refs/heads/main/security/apiiroltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiiroltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiiro.com
coverage:
  checked: 2026-09-25
  detail: All attempted OpenAPI endpoints on known hosts returned 403 or other errors, and no documentation host was discovered.
  evidence:
  - status: 403
    url: https://apiiro.com/openapi.json
  - status: 302
    url: https://idp.apiiro.com/openapi.json
  - status: 404
    url: https://status.apiiro.com/openapi.json
  - status: 403
    url: https://support.apiiro.com/openapi.json
  - status: 404
    url: https://partners.apiiro.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Apiiroltd, operating as Apiiro, provides an AI‑driven application security platform that secures the entire software development lifecycle. Their solution offers continuous code analysis, runtime protection, and automated remediation for vulnerabilities in code, APIs, and AI agents. Targeting enterprise DevOps and security teams, Apiiro integrates with CI/CD pipelines, cloud environments, and developer tools to deliver real‑time risk insights and automated fixes, helping organizations prevent breaches before they happen.
layout: provider
modified: '2026-09-25'
name: Apiiroltd
nav: Providers
network: true
overview: 'Apiiroltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Application-Protection, DevOps, Artificial Intelligence, and Enterprise.


  Apiiroltd''s developer surface includes support and 14 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apiiroltd Domain Security
  slug: apiiroltd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apiiroltd Vulnerability Disclosure
  slug: apiiroltd-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Apiiroltd Trust Center
  slug: apiiroltd-trust-center
  summary_line: SOC 2, ISO 27001
slug: apiiroltd
tags:
- Security
- Application-Protection
- DevOps
- Artificial Intelligence
- Enterprise
website: https://apiiro.com
---
