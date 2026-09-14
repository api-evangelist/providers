---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://fasab.gov/wp-json
  baseurl_source: declared
  description: The anonymous, read-only WordPress REST API behind fasab.gov. Serves FASAB's site pages (Standards & Guidance, handbook-by-chapter, active and archived projects, board and ASIC meeting material, brief
  name: FASAB Public Content API (WordPress REST)
  slug: federal-accounting-standards-advisory-board-wp-content
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-accounting-standards-advisory-board-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-accounting-standards-advisory-board
- group: company
  title: ''
  type: Website
  url: https://fasab.gov/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/federal-accounting-standards-advisory-board-wp-content-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/federal-accounting-standards-advisory-board-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/federal-accounting-standards-advisory-board-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/federal-accounting-standards-advisory-board-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/federal-accounting-standards-advisory-board-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/federal-accounting-standards-advisory-board-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/federal-accounting-standards-advisory-board-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/federal-accounting-standards-advisory-board-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/federal-accounting-standards-advisory-board-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/federal-accounting-standards-advisory-board-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-accounting-standards-advisory-board-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federal-accounting-standards-advisory-board-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/federal-accounting-standards-advisory-board-wp-content-overlay.yaml
- group: company
  title: ''
  type: Blog
  url: https://fasab.gov/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://fasab.gov/feed/
- group: operate
  title: ''
  type: Support
  url: https://fasab.gov/about-fasab/contact-information/
created: '2024-12-25'
description: The Federal Accounting Standards Advisory Board (FASAB) is the U.S. federal advisory body designated to set generally accepted accounting principles for the federal government and its component reporting entities. FASAB issues Statements of Federal Financial Accounting Standards (SFFAS), technical releases, interpretations and staff implementation guidance, consolidates them into the FASAB Handbook, and runs the public due-process cycle of board and ASIC meetings, active projects and exposure drafts open for comment. FASAB publishes no developer program or specification, but fasab.gov runs on WordPress and serves the WordPress REST API anonymously at https://fasab.gov/wp-json/ — a read-only surface over 402 pages, 214 media records, the site taxonomies and search, whose OpenAPI here was derived from that live route index. The authoritative pronouncements remain PDFs on files.fasab.gov.
examples:
- key_count: 3
  name: Federal Accounting Standards Advisory Board Error 401
  slug: federal-accounting-standards-advisory-board-error-401
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-accounting-standards-advisory-board.png
layout: provider
modified: '2026-09-09'
name: Federal Accounting Standards Advisory Board
nav: Providers
network: true
overview: 'Federal Accounting Standards Advisory Board publishes 1 API on the [APIs.io](https://apis.io/) network: FASAB Public Content API (WordPress REST). Tagged areas include Accounting, Federal-Government, Standards, Financial-Reporting, and Government.


  Federal Accounting Standards Advisory Board''s developer surface includes authentication, engineering blog, support, and 17 more developer resources.'
plans:
- name: Federal Accounting Standards Advisory Board Plans Pricing
  plan_count: 0
  slug: federal-accounting-standards-advisory-board-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Federal Accounting Standards Advisory Board Rate Limits
  slug: federal-accounting-standards-advisory-board-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/screenshots/federal-accounting-standards-advisory-board-2026-06-20T181109.png
security:
- kind: authentication
  name: Federal Accounting Standards Advisory Board Authentication
  slug: federal-accounting-standards-advisory-board-authentication
  summary_line: none/basic · 2 schemes
- kind: domain-security
  name: Federal Accounting Standards Advisory Board Domain Security
  slug: federal-accounting-standards-advisory-board-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: federal-accounting-standards-advisory-board
tags:
- Accounting
- Federal-Government
- Standards
- Financial-Reporting
- Government
- Regulations
- Content
- Publications
website: https://fasab.gov/
---
