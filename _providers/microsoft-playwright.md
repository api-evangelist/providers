---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Microsoft Playwright Agentic Access
  operation_count: 18
  slug: microsoft-playwright-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 4
apis:
- description: Playwright provides a cross-browser automation API for end-to-end testing of web applications. It supports Chromium, Firefox, and WebKit with a single API, enabling reliable testing with auto-wait, ne
  name: Playwright API
  slug: playwright-api
- description: Open-source framework for reliable end-to-end browser testing and web automation supporting Chromium, Firefox, and WebKit. Distributed as a library/CLI; there is no public hosted HTTP API.
  name: Playwright
  slug: playwright
- description: Local stdio Model Context Protocol server (npx @playwright/mcp@latest) exposing 44 documented browser_* tools for LLM-driven browser automation via accessibility snapshots.
  name: Playwright MCP
  slug: playwright-mcp
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The AccountQuotas API from Microsoft Playwright — 2 operation(s) for accountquotas.
  name: Microsoft Playwright Account Quotas API
  slug: microsoft-playwright-accountquotas-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Accounts API from Microsoft Playwright — 8 operation(s) for accounts.
  name: Microsoft Playwright Accounts API
  slug: microsoft-playwright-accounts-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Operations API from Microsoft Playwright — 1 operation(s) for operations.
  name: Microsoft Playwright Operations API
  slug: microsoft-playwright-operations-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Quotas API from Microsoft Playwright — 2 operation(s) for quotas.
  name: Microsoft Playwright Quotas API
  slug: microsoft-playwright-quotas-api
artifact_total: 17
common:
- group: start
  title: ''
  type: Sandbox
  url: https://playwright.dev/mcp/tools/console
- group: agent
  href: https://artifacts.apis.io/microsoft-playwright/agentic-access/microsoft-playwright-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-playwright-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/microsoft-playwright/rules/microsoft-playwright-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-playwright-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-playwright/vocabulary/microsoft-playwright-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-playwright-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-playwright/data-model/microsoft-playwright-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-playwright-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-playwright/errors/microsoft-playwright-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-playwright-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-playwright/conformance/microsoft-playwright-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-playwright-conformance.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-playwright/scopes/microsoft-playwright-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-playwright-scopes.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-playwright/authentication/microsoft-playwright-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-playwright-authentication.yml
- group: build
  href: https://artifacts.apis.io/microsoft-playwright/cli/microsoft-playwright-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-playwright-cli.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-playwright/well-known/microsoft-playwright-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-playwright-www-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-playwright/well-known/microsoft-playwright-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-playwright-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-playwright/hosts/microsoft-playwright-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-playwright-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-playwright/integrations/microsoft-playwright-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-playwright-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-playwright/vendors/microsoft-playwright-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-playwright-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-playwright/packages/microsoft-playwright-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-playwright-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-playwright/packages/microsoft-playwright-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-playwright-packages.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-playwright/plans/microsoft-playwright-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-playwright-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-playwright/finops/microsoft-playwright-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-playwright-finops.yml
- group: operate
  title: ''
  type: Community
  url: https://aka.ms/playwright/discord
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/microsoft/playwright/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/microsoft/playwright/issues
- group: auth
  href: https://artifacts.apis.io/microsoft-playwright/security/microsoft-playwright-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-playwright-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/playwrightweb
- group: start
  title: ''
  type: Portal
  url: https://playwright.dev/
- group: company
  title: ''
  type: Website
  url: https://playwright.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://playwright.dev/docs/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/playwright
- group: start
  title: ''
  type: GettingStarted
  url: https://playwright.dev/docs/intro
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/playwright-mcp
- group: docs
  title: ''
  type: APIReference
  url: https://playwright.dev/docs/api/class-playwright
- group: operate
  title: ''
  type: ChangeLog
  url: https://playwright.dev/docs/release-notes
- group: operate
  title: ''
  type: Support
  url: https://playwright.dev/community/welcome
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/app-testing/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Playwrightdev
created: '2024-01-01'
description: Playwright is Microsoft's open-source (Apache-2.0) browser automation framework for reliable end-to-end testing of web applications, driving Chromium, Firefox and WebKit through one API from Node.js, Python, Java and .NET. It also ships a local stdio MCP server (@playwright/mcp) and an agent-oriented CLI (@playwright/cli); hosted cloud browsers are sold as Playwright Workspaces in Azure App Testing.
finops:
- has_sources: false
  method: generated
  name: Microsoft Playwright Finops
  primary_unit: request
  service_category: API
  slug: microsoft-playwright-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-playwright.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: MCP server; 44 tools listed.
  name: Playwright MCP
  slug: playwright-mcp
modified: '2026-11-04'
name: Microsoft Playwright
nav: Providers
network: true
overview: 'Microsoft Playwright publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Quotas API, Accounts API, Operations API, and 4 more. Tagged areas include Browser Automation, End-to-End Testing, Microsoft, Testing, and Open Source.


  The Microsoft Playwright catalog on APIs.io includes 1 Spectral governance ruleset.


  Microsoft Playwright''s developer surface includes sandbox, authentication, CLI, release notes, developer portal, documentation, getting-started guide, and 30 more developer resources.'
plans:
- name: Microsoft Playwright Plans Pricing
  plan_count: 3
  slug: microsoft-playwright-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Microsoft Playwright Rate Limits
  slug: microsoft-playwright-rate-limits
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Microsoft Playwright API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-playwright-rules
scopes:
- name: Microsoft Playwright Scopes
  scope_count: 2
  slug: microsoft-playwright-scopes
  summary_line: 2 scopes · implicit/authorizationCode
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 30.9
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 41.6
    developer_ergonomics: 73.8
    discoverability: 68.3
    operational_transparency: 31.6
  previous_composite: 23.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/microsoft-playwright/microsoft-playwright-2026-06-20T185519.png
security:
- kind: authentication
  name: Microsoft Playwright Authentication
  slug: microsoft-playwright-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Playwright Domain Security
  slug: microsoft-playwright-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-playwright
tags:
- Browser Automation
- End-to-End Testing
- Microsoft
- Testing
- Open Source
- MCP
- Microsoft Azure
website: https://playwright.dev/
---
