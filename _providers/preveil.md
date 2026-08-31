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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.preveil.com/
- group: docs
  title: ''
  type: Documentation
  url: https://preveil.atlassian.net/wiki/spaces/ESD/overview
- group: operate
  title: ''
  type: Support
  url: https://www.preveil.com/support-page/
- group: operate
  title: ''
  type: HelpCenter
  url: https://servicedesk.preveil.com/servicedesk/customer/portals
- group: company
  title: ''
  type: Blog
  url: https://www.preveil.com/resources/?resource-type=blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PreVeil
- group: commercial
  title: ''
  type: Pricing
  url: https://www.preveil.com/new-pricing-page/
- group: start
  title: ''
  type: SignUp
  url: https://www.preveil.com/createaccount/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.preveil.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.preveil.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.preveil.com/vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/preveil-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/preveil-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/preveil-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.preveil.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/preveil-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/preveil-plans-pricing.yml
- group: build
  title: ''
  type: CLI
  url: cli/preveil-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/preveil-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/preveil-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/preveil-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/preveil-llms.txt
coverage:
  checked: '2026-08-26'
  detail: PreVeil ships end-user encrypted email and file-sharing clients and publishes no developer program at all — there is no api./developer./docs. host in DNS, /openapi.json and every /.well-known/ path 404 on www.preveil.com, the web.preveil.com SPA answers 200 with an HTML shell for every path including /openapi.json and /.well-known/agent-card.json, and a full-text search of PreVeil's own Confluence knowledge base for "API" returns one hit that is an Android API-level requirement; the only documented programmatic surfaces are a bundled Drive Upload CLI that talks to a machine-local daemon and a licensed SIEM Connector appliance that exports logs as syslog.
  evidence:
  - status: 404
    url: https://www.preveil.com/openapi.json
  - status: 404
    url: https://www.preveil.com/.well-known/api-catalog
  - status: 200
    url: https://web.preveil.com/openapi.json
  - status: 404
    url: https://collections.preveil.com/openapi.json
  - status: 200
    url: https://preveil.atlassian.net/wiki/rest/api/search?cql=space=ESD%20and%20text~%22API%22
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'PreVeil is a Boston-based end-to-end encrypted email and file-sharing platform built for organizations that must protect Controlled Unclassified Information (CUI) and meet CMMC 2.0 Level 2, DFARS 252.204-7012, ITAR, NIST SP 800-171, HIPAA and GDPR obligations. Its architecture removes the central point of compromise: every message and file is encrypted on the endpoint with per-user keys the service never holds, privileged administrative actions require multi-party cryptographic consent through Approval Groups, and there are no passwords to phish. The platform ships PreVeil Drive (encrypted file sharing and sync through Windows Explorer, Mac Finder or a browser), PreVeil Email (which layers onto existing Outlook, Apple Mail and Gmail clients), PreVeil Express for free browser-based external collaboration, an Admin Console with tamper-proof activity logging, e-discovery and device management, a licensed SIEM Connector appliance that exports those logs in syslog format, and a
  Compliance Accelerator and GRC platform for CMMC documentation. PreVeil publishes no public developer API, SDK or OpenAPI definition; its documented programmatic surface is the first-party PreVeil Drive Upload command-line tool and the SIEM Connector.'
image: https://www.preveil.com/wp-content/uploads/2020/11/logo-preveil.svg
layout: provider
modified: '2026-08-26'
name: PreVeil
nav: Providers
network: true
overview: 'PreVeil is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Encryption, End-to-End Encryption, Email, File Sharing, and Security.


  PreVeil''s developer surface includes documentation, support, engineering blog, pricing, signup flow, changelog, CLI, and 15 more developer resources.'
plans:
- name: Preveil Plans Pricing
  plan_count: 5
  slug: preveil-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Preveil Rate Limits
  slug: preveil-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 35.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Preveil Domain Security
  slug: preveil-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Preveil Vulnerability Disclosure
  slug: preveil-vulnerability-disclosure
  summary_line: contact published
slug: preveil
tags:
- Encryption
- End-to-End Encryption
- Email
- File Sharing
- Security
- Compliance
- CMMC
- ITAR
- CUI
- Defense
- Cybersecurity
- Data Protection
website: https://www.preveil.com/
---
