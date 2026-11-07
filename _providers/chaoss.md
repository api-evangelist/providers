---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The CHAOSS Metrics catalog is a community-maintained, structured reference of community-health metrics organized into focus areas (Common, DEI, Risk, Value, Evolution) plus metrics models that compose
  name: CHAOSS Metrics Catalog
  slug: metrics-catalog
- description: GrimoireLab is an open source platform for software development analytics. It pulls data from 30+ data sources (Git, GitHub, GitLab, mailing lists, IRC, Slack, Jira, Bugzilla, etc.) and provides a Pyt
  name: CHAOSS GrimoireLab
  slug: grimoirelab
- description: 8Knot is an open source community analytics dashboard built on the data collected by CollectOSS (formerly Augur) that provides ready-made visualizations of CHAOSS metrics for stakeholders evaluating o
  name: CHAOSS 8Knot Dashboard
  slug: 8knot
- baseURL: https://collectoss.example.com/api/unstable
  baseurl_source: declared
  description: The complexity API from CHAOSS — 6 operation(s) for complexity.
  name: CHAOSS Complexity API
  slug: chaoss-complexity-api
- baseURL: https://collectoss.example.com/api/unstable
  baseurl_source: declared
  description: The DEI Badging API from CHAOSS — 2 operation(s) for dei badging.
  name: CHAOSS DEI Badging API
  slug: chaoss-dei-badging-api
- baseURL: https://collectoss.example.com/api/unstable
  baseurl_source: declared
  description: The evolution API from CHAOSS — 52 operation(s) for evolution.
  name: CHAOSS Evolution API
  slug: chaoss-evolution-api
- baseURL: https://collectoss.example.com/api/unstable
  baseurl_source: declared
  description: The experimental API from CHAOSS — 26 operation(s) for experimental.
  name: CHAOSS Experimental API
  slug: chaoss-experimental-api
- baseURL: https://collectoss.example.com/api/unstable
  baseurl_source: declared
  description: The login API from CHAOSS — 2 operation(s) for login.
  name: CHAOSS Login API
  slug: chaoss-login-api
- baseURL: https://collectoss.example.com/api/unstable
  baseurl_source: declared
  description: The risk API from CHAOSS — 21 operation(s) for risk.
  name: CHAOSS Risk API
  slug: chaoss-risk-api
- baseURL: https://collectoss.example.com/api/unstable
  baseurl_source: declared
  description: The utility API from CHAOSS — 8 operation(s) for utility.
  name: CHAOSS Utility API
  slug: chaoss-utility-api
- baseURL: https://collectoss.example.com/api/unstable
  baseurl_source: declared
  description: The value API from CHAOSS — 8 operation(s) for value.
  name: CHAOSS Value API
  slug: chaoss-value-api
- baseURL: https://collectoss.example.com/api/unstable
  baseurl_source: declared
  description: The visualizations API from CHAOSS — 12 operation(s) for visualizations.
  name: CHAOSS Visualizations API
  slug: chaoss-visualizations-api
artifact_total: 64
common:
- group: commercial
  href: https://artifacts.apis.io/chaoss/finops/chaoss-finops.yml
  title: ''
  type: FinOps
  url: finops/chaoss-finops.yml
- group: other
  href: https://artifacts.apis.io/chaoss/overlays/chaoss-collectoss-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/chaoss-collectoss-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/chaoss/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/chaoss/CollectOSS/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/chaoss/.github/blob/main/CODE_OF_CONDUCT.md
- group: auth
  href: https://artifacts.apis.io/chaoss/security/chaoss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chaoss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chaoss.community/
- group: docs
  title: ''
  type: Documentation
  url: https://chaoss.community/kbtopic/all-metrics/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/chaoss
- group: other
  title: ''
  type: WorkingGroups
  url: https://www.chaoss.community/kb/working-groups/
- group: other
  title: ''
  type: Events
  url: https://www.chaoss.community/chaoss-calendar/
- group: company
  title: ''
  type: Blog
  url: https://www.chaoss.community/blog/
- group: docs
  title: ''
  type: PractitionerGuides
  url: https://www.chaoss.community/about-chaoss-practitioner-guides/
- group: other
  title: ''
  type: ParentOrganization
  url: https://www.linuxfoundation.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chaoss.community/kb-getting-started/
- group: operate
  title: ''
  type: Community
  url: https://www.chaoss.community/chaoss-calendar/
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/chaoss-workspace/shared_invite/zt-35ir7w0jr-aiwTPYShbj~mMsMbzhGWWQ
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@CHAOSStube
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chaoss
- group: other
  title: ''
  type: X
  url: https://x.com/chaossproj
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chaoss
- group: operate
  title: ''
  type: Support
  url: https://github.com/chaoss/community/discussions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chaoss.community/data-policies/
- group: design
  title: ''
  type: GovernanceRules
  url: https://www.chaoss.community/governance/
- group: build
  href: https://artifacts.apis.io/chaoss/packages/chaoss-packages.yml
  title: ''
  type: Packages
  url: packages/chaoss-packages.yml
- group: build
  href: https://artifacts.apis.io/chaoss/cli/chaoss-cli.yml
  title: ''
  type: CLI
  url: cli/chaoss-cli.yml
- group: design
  href: https://artifacts.apis.io/chaoss/conventions/chaoss-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chaoss-conventions.yml
- group: design
  href: https://artifacts.apis.io/chaoss/conformance/chaoss-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chaoss-conformance.yml
- group: design
  href: https://artifacts.apis.io/chaoss/lifecycle/chaoss-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/chaoss-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/chaoss/changelog/chaoss-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chaoss-changelog.yml
- group: start
  href: https://artifacts.apis.io/chaoss/sandbox/chaoss-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/chaoss-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/chaoss/scopes/chaoss-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/chaoss-scopes.yml
- group: commercial
  href: https://artifacts.apis.io/chaoss/plans/chaoss-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chaoss-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/chaoss/rate-limits/chaoss-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chaoss-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/chaoss/llms/chaoss-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chaoss-llms.txt
- group: auth
  href: https://artifacts.apis.io/chaoss/security/chaoss-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/chaoss-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chaoss/security/chaoss-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chaoss-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Tools
  url: ''
- group: other
  title: ''
  type: WorkingGroups
  url: ''
created: '2026-03-16'
description: 'CHAOSS (Community Health Analytics in Open Source Software) is a Linux Foundation project that develops metrics, methodologies, software, and practitioner guides for measuring and improving open source community health and sustainability. It maintains a metrics catalog organized into focus areas (Common, DEI, Risk, Value, Evolution) plus metrics models, and ships the open source software that computes them: CollectOSS, a Python data-collection tool that stores forge data in PostgreSQL and exposes a 137-operation REST API of CHAOSS-aligned metrics, and GrimoireLab, a Python toolchain and OpenSearch dashboard that ingests 30+ data sources. Both are self-hosted — CHAOSS operates no hosted API and sells nothing. CHAOSS also runs the DEI Project Badging program and publishes practitioner guides for OSPOs, maintainers and funders. Augur, formerly the CHAOSS reference implementation, left the project in March 2026 and was superseded by CollectOSS.'
features:
- name: Community Health Metrics
- name: Metrics Models
- name: DEI Metrics
- name: Risk Metrics
- name: Value Metrics
- name: Evolution Metrics
- name: Common Metrics
- name: Open Source Software
- name: Practitioner Guides
- name: Working Groups
- name: Reference Implementations
- name: REST API (CollectOSS)
- name: Data Pipeline (GrimoireLab)
- name: Dashboards (8Knot, Bitergia)
- name: SaaS Adopter Services
finops:
- has_sources: false
  method: generated
  name: Chaoss Finops
  primary_unit: request
  service_category: API
  slug: chaoss-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chaoss.png
integrations:
- name: GitHub
- name: GitLab
- name: Bitbucket
- name: Git
- name: Mailing Lists
- name: Jira
- name: Bugzilla
- name: Discourse
- name: Slack
- name: IRC
- name: Stack Exchange
- name: Meetup
- name: Linux Foundation
- name: CNCF
- name: Apache Software Foundation
- name: OpenSSF
layout: provider
modified: '2026-09-05'
name: CHAOSS
nav: Providers
network: true
overview: 'CHAOSS publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Complexity API, DEI Badging API, Evolution API, and 9 more. Tagged areas include Analytics, Community Health, DEI, Linux Foundation, and Metrics.


  The CHAOSS catalog on APIs.io includes 1 Spectral governance ruleset.


  CHAOSS''s developer surface includes documentation, GitHub presence, engineering blog, getting-started guide, YouTube channel, support, CLI, and 30 more developer resources.'
plans:
- name: Chaoss Plans Pricing
  plan_count: 0
  slug: chaoss-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Chaoss Rate Limits
  slug: chaoss-rate-limits
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: CHAOSS API Rules
  rule_count: 32
  severity_counts:
    error: 24
    hint: 0
    info: 1
    warn: 7
  slug: chaoss-rules
scopes:
- name: Chaoss Scopes
  scope_count: 0
  slug: chaoss-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 38.3
    developer_ergonomics: 63.7
    discoverability: 64.3
    operational_transparency: 28.9
  previous_composite: 39.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 34.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/chaoss/chaoss-2026-06-20T174222.png
security:
- kind: authentication
  name: Chaoss Authentication
  slug: chaoss-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chaoss Domain Security
  slug: chaoss-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Chaoss Vulnerability Disclosure
  slug: chaoss-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 3
skills:
- name: chaoss-collectoss-assess-repository-health
  slug: chaoss-collectoss-assess-repository-health
- name: chaoss-collectoss-authenticate
  slug: chaoss-collectoss-authenticate
- name: chaoss-collectoss-compare-repo-group
  slug: chaoss-collectoss-compare-repo-group
slug: chaoss
tags:
- Analytics
- Community Health
- DEI
- Linux Foundation
- Metrics
- Observability
- Open Source
- Risk Management
- Sustainability
use_cases:
- name: Open Source Project Health Assessment
- name: Contributor Sustainability Analysis
- name: DEI in Open Source Communities
- name: Open Source Risk and Security Assessment
- name: Open Source Investment ROI
- name: Funding Impact Measurement
- name: Community Onboarding Improvement
- name: Foundation-Level Reporting
- name: OSPO Health Reporting
- name: Maintainer Burnout Detection
website: https://chaoss.community/
---
