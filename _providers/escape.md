---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 104
  human_in_the_loop: 0
  name: Escape Agentic Access
  operation_count: 168
  slug: escape-agentic-access
  summary_line: 168 operations · 104 acting
api_count: 2
apis:
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Attack Surface Management Trigger and manage ASM discovery scans on your attack surface. See [our documentation](https://docs.escape.tech/documentation/asm/) for more details.
  name: Escape Asm API
  slug: escape-asm-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Manage every discovered Assets. The public API provide basic CRUDs operations for all available assets. See [our documentation](https://docs.escape.tech/documentation/asm/asset-management/) for more d
  name: Escape Assets API
  slug: escape-assets-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: List audit logs. The public API provides endpoints to list audit logs. See [our documentation](https://docs.escape.tech/documentation/enterprise/audit-logs/) for more details.
  name: Escape Audit API
  slug: escape-audit-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Beta These endpoints are in beta and are subject to change.
  name: Escape Beta API
  slug: escape-beta-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Read scan inbox emails. The public API provides endpoints to list inbox emails and read their raw content without exposing storage links.
  name: Escape Emails API
  slug: escape-emails-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Manage events. The public API provides basic CRUDs operations to manage events.
  name: Escape Events API
  slug: escape-events-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Manage 3rd party integrations. The public API provide basic CRUDs operations for all available integrations. See [our documentation](https://https://docs.escape.tech/documentation/asm/integrations/) f
  name: Escape Integrations API
  slug: escape-integrations-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Manage issues. Identify, prioritize, and remediate the security issues and sensitive data exposures uncovered during ASM and DAST scanning See [our documentation](https://docs.escape.tech/documentatio
  name: Escape Issues API
  slug: escape-issues-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Asynchronous jobs. Trigger export jobs and poll for completion and artefacts.
  name: Escape Jobs API
  slug: escape-jobs-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: A Location is a proxy environment through which Escape sends requests. The public API provide basic CRUDs operations for your private locations. See [our documentation](https://docs.escape.tech/docume
  name: Escape Locations API
  slug: escape-locations-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: A Profile is a configuration for the DAST scanning feature. It includes various parameters such as authentication details, environment settings, a schema... Profiles allow you to start scans on an end
  name: Escape Profiles API
  slug: escape-profiles-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Projects Management The public API provides CRUDs operations to manage projects.
  name: Escape Projects API
  slug: escape-projects-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Roles Management The public API provides CRUDs operations to manage roles.
  name: Escape Roles API
  slug: escape-roles-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: 'A Scan is a run of the DAST or ASM scanning feature on an profile (DAST/ASM). With the public API, you can trigger scans, track their status, and retrieve their results. See [our documentation](https:'
  name: Escape Scans API
  slug: escape-scans-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Organization Statistics High-level organization security posture statistics.
  name: Escape Statistics API
  slug: escape-statistics-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Manage tags. The public API provides basic CRUDs operations to manage tags.
  name: Escape Tags API
  slug: escape-tags-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Upload helper for Escape Platform. The public API provides endpoints to upload files to the platform.
  name: Escape Upload API
  slug: escape-upload-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Users Management The public API provides CRUDs operations to manage users.
  name: Escape Users API
  slug: escape-users-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Workflows Management The public API provides CRUDs operations to manage workflows.
  name: Escape Workflows API
  slug: escape-workflows-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Copilot chats. Create, list and resume Copilot chats. Only the chats owned by the authenticated user are exposed.
  name: Escape AI Chats API
  slug: escape-aichats-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Compliance frameworks Read compliance posture at organization, application, and scan level, and manage enabled compliance frameworks.
  name: Escape Compliance API
  slug: escape-compliance-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Manage organization knowledge files. The knowledge file library gives AI pentests context about your organization. Upload files with a signed URL, list them, and delete them.
  name: Escape Knowledge Files API
  slug: escape-knowledgefiles-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: 'Organization settings. Manage organization-wide settings: issue SLA policy, AI system prompt, project propagation and scoped webhook export. Scan kill switches are read-only.'
  name: Escape Organization Settings API
  slug: escape-organizationsettings-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Manage regression tests. Create regression tests from a source report, run them, and track their history. A regression test re-validates a finding against an updated codebase.
  name: Escape Regression Tests API
  slug: escape-regressiontests-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: A Retest is a scan that re-validates selected issues on a DAST or AI pentest profile. Start a retest with explicit issue IDs or a filter, then poll status, progress, and per-issue agents (status and o
  name: Escape Retests API
  slug: escape-retests-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: 'Manage security tests. Browse the security tests Escape can run, with their organization configuration (enabled state and custom severity), scanner and asset applicability, description and compliance '
  name: Escape Security Tests API
  slug: escape-securitytests-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Target validations. Start a validation to check that a target (asset) is reachable and in scope, then poll for status and output.
  name: Escape Validations API
  slug: escape-validations-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: 'Manage vault variables. Vault variables are secret references used by scan authentication configs. Values are write-only: they are accepted on create and update, but never returned by the API.'
  name: Escape Vault Variables API
  slug: escape-vaultvariables-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Saved views The public API provides CRUDs operations to manage saved views and list the issues matching an issue view.
  name: Escape Views API
  slug: escape-views-api
- baseURL: https://public.escape.tech/v3
  baseurl_source: declared
  description: Manage your custom rules. The public API provides basic CRUDs operations to manage custom rules. See our documentation for more details.
  name: Escape Custom Rules API
  slug: escape-custom-rules-api
artifact_total: 59
collections:
- collection_type: open
  name: Escape Public Asm API
  slug: open-escape-asm-api
- collection_type: open
  name: Escape Public Asm Assets API
  slug: open-escape-assets-api
- collection_type: open
  name: Escape Public Asm Audit API
  slug: open-escape-audit-api
- collection_type: open
  name: Escape Public Asm Beta API
  slug: open-escape-beta-api
- collection_type: open
  name: Escape Public Asm CustomRules API
  slug: open-escape-customrules-api
- collection_type: open
  name: Escape Public Asm Emails API
  slug: open-escape-emails-api
- collection_type: open
  name: Escape Public Asm Events API
  slug: open-escape-events-api
- collection_type: open
  name: Escape Public Asm Integrations API
  slug: open-escape-integrations-api
- collection_type: open
  name: Escape Public Asm Issues API
  slug: open-escape-issues-api
- collection_type: open
  name: Escape Public Asm Jobs API
  slug: open-escape-jobs-api
- collection_type: open
  name: Escape Public Asm Locations API
  slug: open-escape-locations-api
- collection_type: open
  name: Escape Public Asm Profiles API
  slug: open-escape-profiles-api
- collection_type: open
  name: Escape Public Asm Projects API
  slug: open-escape-projects-api
- collection_type: open
  name: Escape Public Asm Roles API
  slug: open-escape-roles-api
- collection_type: open
  name: Escape Public Asm Scans API
  slug: open-escape-scans-api
- collection_type: open
  name: Escape Public Asm Statistics API
  slug: open-escape-statistics-api
- collection_type: open
  name: Escape Public Asm Tags API
  slug: open-escape-tags-api
- collection_type: open
  name: Escape Public Asm Upload API
  slug: open-escape-upload-api
- collection_type: open
  name: Escape Public Asm Users API
  slug: open-escape-users-api
- collection_type: open
  name: Escape Public Asm Workflows API
  slug: open-escape-workflows-api
- collection_type: open
  name: Escape Public API
  slug: open-escape
common:
- group: commercial
  href: https://artifacts.apis.io/escape/plans/escape-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/escape-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/escape/rate-limits/escape-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/escape-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/escape/finops/escape-finops.yml
  title: ''
  type: FinOps
  url: finops/escape-finops.yml
- group: other
  href: https://artifacts.apis.io/escape/capabilities/escape-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/escape-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/escape/agentic-access/escape-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/escape-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/escape/security/escape-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/escape-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/escape/authentication/escape-authentication.yml
  title: ''
  type: Authentication
  url: authentication/escape-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/escape-technologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/escapetech
- group: docs
  title: ''
  type: Documentation
  url: https://docs.escape.tech/
- group: company
  title: ''
  type: Blog
  url: https://escape.tech/blog/
- group: other
  title: ''
  type: CaseStudies
  url: https://escape.tech/blog/tag/case-study/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://escape.tech/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://escape.tech/terms
- group: company
  title: ''
  type: Website
  url: https://escape.tech/
created: '2025-01-08'
description: Escape was founded in 2020 after one of our co-founders experienced a cyberattack and saw firsthand how vulnerable exposed APIs can be. Driven by a belief in the power of AI to transform cybersecurity, we built a platform that emulates hacker behavior to identify vulnerabilities before they can be exploited. Escape is a DAST (Dynamic Application Security Testing) platform that helps you document all your APIs, detect complex business logic flaws across modern applications like APIs, SPAs, and Microservices, and seamlessly integrate security into your CI/CD pipeline.
finops:
- has_sources: false
  method: generated
  name: Escape Finops
  primary_unit: request
  service_category: API
  slug: escape-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/escape.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.escape.tech over HTTP.
  name: Escape MCP Server
  slug: escape
modified: '2026-05-19'
name: Escape
nav: Providers
network: true
overview: 'Escape publishes 30 API contracts indexed on the [APIs.io](https://apis.io/) network, including Asm API, Assets API, Audit API, and 27 more. Tagged areas include Platform and Security.


  The Escape catalog on APIs.io includes 1 Spectral governance ruleset.


  Escape''s developer surface includes authentication, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Escape Plans Pricing
  plan_count: 3
  slug: escape-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Escape Rate Limits
  slug: escape-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Escape API Rules
  rule_count: 53
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 8
  slug: escape-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 53.2
    developer_ergonomics: 23.8
    discoverability: 60.0
    operational_transparency: 10.5
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 51
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/escape/escape-2026-06-20T180822.png
security:
- kind: authentication
  name: Escape Authentication
  slug: escape-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Escape Domain Security
  slug: escape-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: escape
tags:
- Platform
- Security
website: https://escape.tech/
---
