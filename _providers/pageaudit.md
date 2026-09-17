---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.8
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Pageaudit Agentic Access
  operation_count: 38
  slug: pageaudit-agentic-access
  summary_line: 38 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Apis.json API from PageAudit — 1 operation(s) for apis.json.
  name: PageAudit Apis.json API
  slug: pageaudit-apis-json-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Audit API from PageAudit — 1 operation(s) for audit.
  name: PageAudit Audit API
  slug: pageaudit-audit-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Audits API from PageAudit — 3 operation(s) for audits.
  name: PageAudit Audits API
  slug: pageaudit-audits-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Auth API from PageAudit — 4 operation(s) for auth.
  name: PageAudit Auth API
  slug: pageaudit-auth-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Badge API from PageAudit — 2 operation(s) for badge.
  name: PageAudit Badge API
  slug: pageaudit-badge-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Billing API from PageAudit — 1 operation(s) for billing.
  name: PageAudit Billing API
  slug: pageaudit-billing-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Contact API from PageAudit — 1 operation(s) for contact.
  name: PageAudit Contact API
  slug: pageaudit-contact-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Credito API from PageAudit — 1 operation(s) for credito.
  name: PageAudit Credito API
  slug: pageaudit-credito-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Gate API from PageAudit — 1 operation(s) for gate.
  name: PageAudit Gate API
  slug: pageaudit-gate-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Guest API from PageAudit — 1 operation(s) for guest.
  name: PageAudit Guest API
  slug: pageaudit-guest-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Health API from PageAudit — 1 operation(s) for health.
  name: PageAudit Health API
  slug: pageaudit-health-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Mcp API from PageAudit — 1 operation(s) for mcp.
  name: PageAudit MCP API
  slug: pageaudit-mcp-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Me API from PageAudit — 1 operation(s) for me.
  name: PageAudit Me API
  slug: pageaudit-me-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Metrics API from PageAudit — 1 operation(s) for metrics.
  name: PageAudit Metrics API
  slug: pageaudit-metrics-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Okf API from PageAudit — 1 operation(s) for okf.
  name: PageAudit Okf API
  slug: pageaudit-okf-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The PageAudit API from PageAudit — 1 operation(s) for pageaudit.
  name: PageAudit Page Audit API
  slug: pageaudit-pageaudit-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The R API from PageAudit — 1 operation(s) for r.
  name: PageAudit R API
  slug: pageaudit-r-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Shared API from PageAudit — 1 operation(s) for shared.
  name: PageAudit Shared API
  slug: pageaudit-shared-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Tabs API from PageAudit — 3 operation(s) for tabs.
  name: PageAudit Tabs API
  slug: pageaudit-tabs-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Tools API from PageAudit — 4 operation(s) for tools.
  name: PageAudit Tools API
  slug: pageaudit-tools-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The Visit API from PageAudit — 1 operation(s) for visit.
  name: PageAudit Visit API
  slug: pageaudit-visit-api
- baseURL: https://pageaudit.online
  baseurl_source: declared
  description: The .well Known API from PageAudit — 1 operation(s) for .well known.
  name: PageAudit .well Known API
  slug: pageaudit-well-known-api
artifact_total: 30
common:
- group: agent
  title: ''
  type: AgentSkill
  url: https://pageaudit.online/okf/index.md
- group: agent
  title: ''
  type: MCPServer
  url: https://pageaudit.online/mcp
- group: company
  title: ''
  type: Website
  url: https://pageaudit.online/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/mcp/pageaudit-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pageaudit-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/security/pageaudit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pageaudit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://pageaudit.online/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/security/pageaudit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pageaudit-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/agentic-access/pageaudit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pageaudit-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/authentication/pageaudit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pageaudit-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/well-known/pageaudit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pageaudit-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/well-known/pageaudit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pageaudit-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/mcp/pageaudit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pageaudit-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/llms/pageaudit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pageaudit-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/overlays/pageaudit-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pageaudit-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/conformance/pageaudit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pageaudit-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/errors/pageaudit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pageaudit-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/lifecycle/pageaudit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pageaudit-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/conventions/pageaudit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pageaudit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/conventions/pageaudit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/pageaudit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/components/pageaudit-components.yml
  title: ''
  type: Components
  url: components/pageaudit-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/data-model/pageaudit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pageaudit-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/plans/pageaudit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pageaudit-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://pageaudit.online/api/billing
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pageaudit/refs/heads/main/rate-limits/pageaudit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pageaudit-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pageaudit.online/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pageaudit.online/privacy
created: '2026-09-05'
description: An agent-first technical SEO auditor that checks a page's search appearance, sharing previews and technical issues, prioritizes fixes, and delivers ready-to-apply patches for head tags, robots and sitemap. Every UI screen has an equivalent endpoint and every resource carries its own API URL.
image: https://pageaudit.online/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: PageAudit MCP Server
  slug: pageaudit-mcp-server
- description: ''
  name: PageAudit
  slug: pageaudit
modified: '2026-09-07'
name: PageAudit
nav: Providers
network: true
overview: 'PageAudit publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Apis.json API, Audit API, Audits API, and 19 more. Tagged areas include Technical SEO, SEO auditing, Developer Tools, agent-native, and MCP.


  PageAudit''s developer surface includes authentication, pricing, and 25 more developer resources.'
plans:
- name: Pageaudit Plans Pricing
  plan_count: 3
  slug: pageaudit-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Pageaudit Rate Limits
  slug: pageaudit-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.6
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 53.6
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 36.8
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Pageaudit Authentication
  slug: pageaudit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pageaudit Domain Security
  slug: pageaudit-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Pageaudit Vulnerability Disclosure
  slug: pageaudit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pageaudit
tags:
- Technical SEO
- SEO auditing
- Developer Tools
- agent-native
- MCP
- x402
website: https://pageaudit.online/
---
