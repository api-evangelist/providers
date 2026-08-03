---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 126
  human_in_the_loop: 4
  name: Nuclei Agentic Access
  operation_count: 273
  slug: nuclei-agentic-access
  summary_line: 273 operations · 126 acting · 4 human-in-the-loop
api_count: 36
apis:
- description: Nuclei is an open source vulnerability scanner from ProjectDiscovery that uses YAML-based templates to find security issues in APIs, web apps, and infrastructure.
  name: Nuclei
  slug: nuclei
- description: The agents API from Nuclei — 4 operation(s) for agents.
  name: Nuclei agents API
  slug: nuclei-agents-api
- description: The Asset API from Nuclei — 12 operation(s) for asset.
  name: Nuclei Asset API
  slug: nuclei-asset-api
- description: The assets API from Nuclei — 9 operation(s) for assets.
  name: Nuclei assets API
  slug: nuclei-assets-api
- description: The automations API from Nuclei — 2 operation(s) for automations.
  name: Nuclei automations API
  slug: nuclei-automations-api
- description: The billing API from Nuclei — 1 operation(s) for billing.
  name: Nuclei billing API
  slug: nuclei-billing-api
- description: The chaos API from Nuclei — 3 operation(s) for chaos.
  name: Nuclei chaos API
  slug: nuclei-chaos-api
- description: The configurations API from Nuclei — 7 operation(s) for configurations.
  name: Nuclei configurations API
  slug: nuclei-configurations-api
- description: The deprecated API from Nuclei — 3 operation(s) for deprecated.
  name: Nuclei deprecated API
  slug: nuclei-deprecated-api
- description: The domains API from Nuclei — 2 operation(s) for domains.
  name: Nuclei domains API
  slug: nuclei-domains-api
- description: The elog API from Nuclei — 1 operation(s) for elog.
  name: Nuclei elog API
  slug: nuclei-elog-api
- description: The enumeration API from Nuclei — 2 operation(s) for enumeration.
  name: Nuclei enumeration API
  slug: nuclei-enumeration-api
- description: The enumerations API from Nuclei — 20 operation(s) for enumerations.
  name: Nuclei enumerations API
  slug: nuclei-enumerations-api
- description: The export API from Nuclei — 4 operation(s) for export.
  name: Nuclei export API
  slug: nuclei-export-api
- description: The history API from Nuclei — 1 operation(s) for history.
  name: Nuclei history API
  slug: nuclei-history-api
- description: The internal API from Nuclei — 33 operation(s) for internal.
  name: Nuclei internal API
  slug: nuclei-internal-api
- description: The Leaks API from Nuclei — 5 operation(s) for leaks.
  name: Nuclei Leaks API
  slug: nuclei-leaks-api
- description: The oauth API from Nuclei — 5 operation(s) for oauth.
  name: Nuclei oauth API
  slug: nuclei-oauth-api
- description: The Payment API from Nuclei — 1 operation(s) for payment.
  name: Nuclei Payment API
  slug: nuclei-payment-api
- description: The results API from Nuclei — 7 operation(s) for results.
  name: Nuclei results API
  slug: nuclei-results-api
- description: The retests API from Nuclei — 2 operation(s) for retests.
  name: Nuclei retests API
  slug: nuclei-retests-api
- description: The scan API from Nuclei — 5 operation(s) for scan.
  name: Nuclei scan API
  slug: nuclei-scan-api
- description: The scan_log API from Nuclei — 3 operation(s) for scan_log.
  name: Nuclei scan_log API
  slug: nuclei-scan-log-api
- description: The Scans API from Nuclei — 24 operation(s) for scans.
  name: Nuclei Scans API
  slug: nuclei-scans-api
- description: The stats API from Nuclei — 1 operation(s) for stats.
  name: Nuclei stats API
  slug: nuclei-stats-api
- description: The tasks API from Nuclei — 2 operation(s) for tasks.
  name: Nuclei tasks API
  slug: nuclei-tasks-api
- description: The Team API from Nuclei — 2 operation(s) for team.
  name: Nuclei Team API
  slug: nuclei-team-api
- description: The Template API from Nuclei — 4 operation(s) for template.
  name: Nuclei Template API
  slug: nuclei-template-api
- description: The template/v2 API from Nuclei — 1 operation(s) for template/v2.
  name: Nuclei template/v2 API
  slug: nuclei-template-v2-api
- description: The templates API from Nuclei — 12 operation(s) for templates.
  name: Nuclei templates API
  slug: nuclei-templates-api
- description: The usage API from Nuclei — 1 operation(s) for usage.
  name: Nuclei usage API
  slug: nuclei-usage-api
- description: The User API from Nuclei — 3 operation(s) for user.
  name: Nuclei User API
  slug: nuclei-user-api
- description: The users API from Nuclei — 12 operation(s) for users.
  name: Nuclei users API
  slug: nuclei-users-api
- description: The vuln API from Nuclei — 1 operation(s) for vuln.
  name: Nuclei vuln API
  slug: nuclei-vuln-api
- description: The Vulnerability API from Nuclei — 9 operation(s) for vulnerability.
  name: Nuclei Vulnerability API
  slug: nuclei-vulnerability-api
- description: The Vulns API from Nuclei — 2 operation(s) for vulns.
  name: Nuclei Vulns API
  slug: nuclei-vulns-api
artifact_total: 45
collections:
- collection_type: open
  name: PDCP API
  slug: open-nuclei
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nuclei-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nuclei-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nuclei-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuclei-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nuclei-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nuclei.projectdiscovery.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.projectdiscovery.io/tools/nuclei/overview
- group: docs
  title: ''
  type: Reference
  url: https://docs.projectdiscovery.io/api-reference/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/projectdiscovery
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/projectdiscovery/nuclei
- group: other
  title: ''
  type: Templates
  url: https://github.com/projectdiscovery/nuclei-templates
- group: other
  title: ''
  type: Cloud
  url: https://cloud.projectdiscovery.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.projectdiscovery.io/rss/
created: '2026-03-25'
description: Nuclei is an open source vulnerability scanner from ProjectDiscovery that uses YAML-based templates to find security issues in APIs, web apps, and infrastructure. It supports multiple protocols (HTTP, DNS, TCP, file), parallel scanning, CI/CD integration, and ships with thousands of community-contributed templates. The ProjectDiscovery Cloud Platform exposes a REST API for managing templates, scans, vulnerabilities, leaks, asset discovery, exports, and more.
finops:
- name: Nuclei Finops
  service_category: API
  slug: nuclei-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuclei.png
layout: provider
modified: '2026-05-19'
name: Nuclei
nav: Providers
network: true
overview: 'Nuclei publishes 35 APIs on the [APIs.io](https://apis.io/) network, including agents API, Asset API, assets API, and 32 more. Tagged areas include Security Testing, Testing, Vulnerability Scanner, DAST, and Open Source.


  Nuclei''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Nuclei Plans Pricing
  plan_count: 3
  slug: nuclei-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Nuclei Rate Limits
  slug: nuclei-rate-limits
score:
  band: thin
  composite: 40.6
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.7
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuclei/refs/heads/main/screenshots/nuclei-2026-06-20T190508.png
security:
- kind: authentication
  name: Nuclei Authentication
  slug: nuclei-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nuclei Domain Security
  slug: nuclei-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nuclei Vulnerability Disclosure
  slug: nuclei-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nuclei Trust Center
  slug: nuclei-trust-center
  summary_line: SOC 2
slug: nuclei
tags:
- Security Testing
- Testing
- Vulnerability Scanner
- DAST
- Open Source
website: https://nuclei.projectdiscovery.io
---
