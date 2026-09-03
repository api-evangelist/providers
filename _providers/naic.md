---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Naic Agentic Access
  operation_count: 569
  slug: naic-agentic-access
  summary_line: 569 operations
api_count: 73
apis:
- description: The NAIC-operated SERFF (System for Electronic Rates & Forms Filing) platform exposes machine integration services to filers, state regulators and filing vendors. The SERFF Technical Support Checklist
  name: SERFF Web Services
  slug: serff-web-services
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: action entity resources exposed by the NAIC JSON:API.
  name: NAIC Action API
  slug: naic-action-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: base_field_override entity resources exposed by the NAIC JSON:API.
  name: NAIC Base Field Override API
  slug: naic-base-field-override-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: block entity resources exposed by the NAIC JSON:API.
  name: NAIC Block API
  slug: naic-block-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Reusable content blocks used to compose NAIC pages.
  name: NAIC Block Content API
  slug: naic-block-content-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: block_content_type entity resources exposed by the NAIC JSON:API.
  name: NAIC Block Content Type API
  slug: naic-block-content-type-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: classy_paragraphs_style entity resources exposed by the NAIC JSON:API.
  name: NAIC Classy Paragraphs Style API
  slug: naic-classy-paragraphs-style-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Comment entities.
  name: NAIC Comment API
  slug: naic-comment-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: comment_type entity resources exposed by the NAIC JSON:API.
  name: NAIC Comment Type API
  slug: naic-comment-type-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Site-wide configuration content, including the sitewide alert.
  name: NAIC Config Pages API
  slug: naic-config-pages-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: config_pages_type entity resources exposed by the NAIC JSON:API.
  name: NAIC Config Pages Type API
  slug: naic-config-pages-type-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: configurable_language entity resources exposed by the NAIC JSON:API.
  name: NAIC Configurable Language API
  slug: naic-configurable-language-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: crop entity resources exposed by the NAIC JSON:API.
  name: NAIC Crop API
  slug: naic-crop-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: crop_type entity resources exposed by the NAIC JSON:API.
  name: NAIC Crop Type API
  slug: naic-crop-type-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: date_format entity resources exposed by the NAIC JSON:API.
  name: NAIC Date Format API
  slug: naic-date-format-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: The JSON:API entry point.
  name: NAIC Discovery API
  slug: naic-discovery-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: editor entity resources exposed by the NAIC JSON:API.
  name: NAIC Editor API
  slug: naic-editor-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: embed_button entity resources exposed by the NAIC JSON:API.
  name: NAIC Embed Button API
  slug: naic-embed-button-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: entity_browser entity resources exposed by the NAIC JSON:API.
  name: NAIC Entity Browser API
  slug: naic-entity-browser-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: entity_extra_field entity resources exposed by the NAIC JSON:API.
  name: NAIC Entity Extra Field API
  slug: naic-entity-extra-field-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: entity_form_display entity resources exposed by the NAIC JSON:API.
  name: NAIC Entity Form Display API
  slug: naic-entity-form-display-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: entity_form_mode entity resources exposed by the NAIC JSON:API.
  name: NAIC Entity Form Mode API
  slug: naic-entity-form-mode-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: entity_view_display entity resources exposed by the NAIC JSON:API.
  name: NAIC Entity View Display API
  slug: naic-entity-view-display-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: entity_view_mode entity resources exposed by the NAIC JSON:API.
  name: NAIC Entity View Mode API
  slug: naic-entity-view-mode-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Event entities.
  name: NAIC Event Entity API
  slug: naic-event-entity-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Feeds importer configuration for state contacts, departments and meeting calendars.
  name: NAIC Feeds Feed API
  slug: naic-feeds-feed-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: feeds_feed_type entity resources exposed by the NAIC JSON:API.
  name: NAIC Feeds Feed Type API
  slug: naic-feeds-feed-type-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: feeds_subscription entity resources exposed by the NAIC JSON:API.
  name: NAIC Feeds Subscription API
  slug: naic-feeds-subscription-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: field_config entity resources exposed by the NAIC JSON:API.
  name: NAIC Field Config API
  slug: naic-field-config-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: field_storage_config entity resources exposed by the NAIC JSON:API.
  name: NAIC Field Storage Config API
  slug: naic-field-storage-config-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Uploaded file entities backing the media entities.
  name: NAIC File API
  slug: naic-file-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: filter_format entity resources exposed by the NAIC JSON:API.
  name: NAIC Filter Format API
  slug: naic-filter-format-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: image_style entity resources exposed by the NAIC JSON:API.
  name: NAIC Image Style API
  slug: naic-image-style-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: imce_profile entity resources exposed by the NAIC JSON:API.
  name: NAIC Imce Profile API
  slug: naic-imce-profile-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: language_content_settings entity resources exposed by the NAIC JSON:API.
  name: NAIC Language Content Settings API
  slug: naic-language-content-settings-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: layout_builder_browser_block entity resources exposed by the NAIC JSON:API.
  name: NAIC Layout Builder Browser Block API
  slug: naic-layout-builder-browser-block-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: layout_builder_browser_blockcat entity resources exposed by the NAIC JSON:API.
  name: NAIC Layout Builder Browser Blockcat API
  slug: naic-layout-builder-browser-blockcat-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: linkit_profile entity resources exposed by the NAIC JSON:API.
  name: NAIC Linkit Profile API
  slug: naic-linkit-profile-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Media entities — documents (PDF publications, reports), images, video and audio.
  name: NAIC Media API
  slug: naic-media-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: media_type entity resources exposed by the NAIC JSON:API.
  name: NAIC Media Type API
  slug: naic-media-type-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: menu entity resources exposed by the NAIC JSON:API.
  name: NAIC Menu API
  slug: naic-menu-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Site navigation menu links.
  name: NAIC Menu Link Content API
  slug: naic-menu-link-content-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: metatag_defaults entity resources exposed by the NAIC JSON:API.
  name: NAIC Metatag Defaults API
  slug: naic-metatag-defaults-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Drupal content nodes — the NAIC's articles, committee pages, publications pages, state insurance department contacts, newsletters, calendars and generic pages.
  name: NAIC Node API
  slug: naic-node-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: node_type entity resources exposed by the NAIC JSON:API.
  name: NAIC Node Type API
  slug: naic-node-type-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Paragraph entities — the composable page building blocks.
  name: NAIC Paragraph API
  slug: naic-paragraph-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: paragraphs_type entity resources exposed by the NAIC JSON:API.
  name: NAIC Paragraphs Type API
  slug: naic-paragraphs-type-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: path_alias entity resources exposed by the NAIC JSON:API.
  name: NAIC Path Alias API
  slug: naic-path-alias-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: pathauto_pattern entity resources exposed by the NAIC JSON:API.
  name: NAIC Pathauto Pattern API
  slug: naic-pathauto-pattern-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: print_engine entity resources exposed by the NAIC JSON:API.
  name: NAIC Print Engine API
  slug: naic-print-engine-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: rdf_mapping entity resources exposed by the NAIC JSON:API.
  name: NAIC Rdf Mapping API
  slug: naic-rdf-mapping-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: redirect entity resources exposed by the NAIC JSON:API.
  name: NAIC Redirect API
  slug: naic-redirect-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: rest_resource_config entity resources exposed by the NAIC JSON:API.
  name: NAIC Rest Resource Config API
  slug: naic-rest-resource-config-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: search_api_index entity resources exposed by the NAIC JSON:API.
  name: NAIC Search API Index API
  slug: naic-search-api-index-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: search_api_server entity resources exposed by the NAIC JSON:API.
  name: NAIC Search API Server API
  slug: naic-search-api-server-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: search_api_task entity resources exposed by the NAIC JSON:API.
  name: NAIC Search API Task API
  slug: naic-search-api-task-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: settings entity resources exposed by the NAIC JSON:API.
  name: NAIC Settings API
  slug: naic-settings-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: shortcut entity resources exposed by the NAIC JSON:API.
  name: NAIC Shortcut API
  slug: naic-shortcut-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: shortcut_set entity resources exposed by the NAIC JSON:API.
  name: NAIC Shortcut Set API
  slug: naic-shortcut-set-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: simple_sitemap entity resources exposed by the NAIC JSON:API.
  name: NAIC Simple Sitemap API
  slug: naic-simple-sitemap-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: simple_sitemap_engine entity resources exposed by the NAIC JSON:API.
  name: NAIC Simple Sitemap Engine API
  slug: naic-simple-sitemap-engine-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: simple_sitemap_type entity resources exposed by the NAIC JSON:API.
  name: NAIC Simple Sitemap Type API
  slug: naic-simple-sitemap-type-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: slick entity resources exposed by the NAIC JSON:API.
  name: NAIC Slick API
  slug: naic-slick-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: Controlled vocabularies — model laws, insurance types, states, committees, publications, research topics and the rest of the NAIC's classification terms.
  name: NAIC Taxonomy Term API
  slug: naic-taxonomy-term-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: taxonomy_vocabulary entity resources exposed by the NAIC JSON:API.
  name: NAIC Taxonomy Vocabulary API
  slug: naic-taxonomy-vocabulary-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: toolbar_menu_element entity resources exposed by the NAIC JSON:API.
  name: NAIC Toolbar Menu Element API
  slug: naic-toolbar-menu-element-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: User entities (public fields only for anonymous callers).
  name: NAIC User API
  slug: naic-user-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: user_role entity resources exposed by the NAIC JSON:API.
  name: NAIC User Role API
  slug: naic-user-role-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: view entity resources exposed by the NAIC JSON:API.
  name: NAIC View API
  slug: naic-view-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: webform entity resources exposed by the NAIC JSON:API.
  name: NAIC Webform API
  slug: naic-webform-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: webform_options entity resources exposed by the NAIC JSON:API.
  name: NAIC Webform Options API
  slug: naic-webform-options-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: webform_submission entity resources exposed by the NAIC JSON:API.
  name: NAIC Webform Submission API
  slug: naic-webform-submission-api
- baseURL: https://services.serff.com/
  baseurl_source: declared
  description: workflow entity resources exposed by the NAIC JSON:API.
  name: NAIC Workflow API
  slug: naic-workflow-api
artifact_total: 82
collections:
- collection_type: open
  name: NAIC Content JSON:API
  slug: open-naic-content-jsonapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/naic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/naic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/naic-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/naic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/naic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/naic-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/naic-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/naic-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/naic-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/naic-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://content.naic.org/
- group: company
  title: ''
  type: About
  url: https://content.naic.org/about
- group: company
  title: ''
  type: Blog
  url: https://content.naic.org/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://content.naic.org/insurance-topics
- group: other
  title: ''
  type: Publications
  url: https://content.naic.org/publications
- group: start
  title: ''
  type: Portal
  url: https://www.serff.com/
- group: start
  title: ''
  type: Portal
  url: https://sbs.naic.org/
- group: start
  title: ''
  type: Portal
  url: https://isiteplus.naic.org/iSiteUI/faces/pages/Home.xhtml
- group: start
  title: ''
  type: Portal
  url: https://insdata.naic.org/
- group: docs
  title: ''
  type: Documentation
  url: https://content.naic.org/insurance-topics/financial-data-repository
- group: docs
  title: ''
  type: Documentation
  url: https://content.naic.org/cis_consumer_information.htm
- group: docs
  title: ''
  type: Documentation
  url: https://content.naic.org/sites/default/files/naic-technology-services-products-catalog.pdf
- group: operate
  title: ''
  type: Support
  url: https://content.naic.org/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://content.naic.org/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://content.naic.org/application/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://content.naic.org/privacy_statement.htm
created: '2026-07-25'
description: 'The National Association of Insurance Commissioners (NAIC) is the U.S. standard-setting and regulatory support organization created and governed by the chief insurance regulators of the 50 states, the District of Columbia and five territories. It is not a carrier and not a federal regulator - under the McCarran-Ferguson settlement the United States has no national insurance supervisor, so the NAIC is the coordinating body through which state-based regulation is made uniform. It writes the model laws, accounting practices and Annual Statement Blanks that every admitted insurer files against, operates the Financial Data Repository behind those filings, and runs the market infrastructure the industry actually transacts on: SERFF for electronic rate and form filing, State Based Systems (SBS) for producer and company licensing in roughly thirty jurisdictions, iSite+ and myNAIC for regulator analytics, OPTins for premium tax, and consumer-facing lookups such as the Consumer Information
  Source and the Life Insurance Policy Locator. Its lines of business span property and casualty, life and annuity, health, title and fraternal across the United States. Its API posture is partner-gated and closed: there is no developer portal at developer/developers/docs.naic.org (all NXDOMAIN), no documented self-serve API, and no downloadable OpenAPI anywhere on naic.org or serff.com. SERFF does operate real integration services - Legacy SPI (two-way PUSH/PULL), Legacy SIS (one-way PULL) and a Modernized Data API (one-way PULL), in PROD and BETA - but they are named only on a support checklist, provisioned by emailing wsrequest@naic.org, and fronted by Okta login walls. Bulk regulatory data is licensed by contract through idp@naic.org rather than served over an API. There is, however, one real and entirely undocumented public machine surface: content.naic.org runs Drupal 11 and serves a live, anonymously readable JSON:API v1.1 at /jsonapi, whose resource index enumerates 284 resource
  types and exposes the model law corpus with its MDL numbers, the state insurance department regulator directory, committees, insurance topics, publications, CIPR research and the newsroom. The NAIC also publishes a first-party llms.txt declaring AI usage preferences, attribution requirements and crawl limits - so its stated contract with automated consumers is more explicit than its contract with API developers.'
examples:
- key_count: 3
  name: Naic Jsonapi Resource Index
  slug: naic-jsonapi-resource-index
- key_count: 5
  name: Naic Node Article Example
  slug: naic-node-article-example
- key_count: 5
  name: Naic Node State Department Contact Example
  slug: naic-node-state-department-contact-example
- key_count: 5
  name: Naic Taxonomy Model Law Example
  slug: naic-taxonomy-model-law-example
- key_count: 3
  name: Naic Taxonomy States Alabama Example
  slug: naic-taxonomy-states-alabama-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: NAIC
nav: Providers
network: true
overview: 'NAIC publishes 72 APIs on the [APIs.io](https://apis.io/) network, including Action API, Base Field Override API, Block API, and 69 more. Tagged areas include Insurance, United States, Regulator, Market Infrastructure, and Insurance Regulation.


  NAIC''s developer surface includes authentication, code examples, engineering blog, documentation, developer portal, support, and 22 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 73.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 16.5
    developer_ergonomics: 39.9
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 73
      marker_coverage: 100.0
      total: 73
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/naic/refs/heads/main/screenshots/naic-2026-08-07T184609.png
security:
- kind: authentication
  name: Naic Authentication
  slug: naic-authentication
  summary_line: none/cookie/saml-oidc-sso · 0 schemes
- kind: domain-security
  name: Naic Domain Security
  slug: naic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: naic
tags:
- Insurance
- United States
- Regulator
- Market Infrastructure
- Insurance Regulation
- Property and Casualty
- Life Insurance
- Health Insurance
- Producer Licensing
- Rate and Form Filing
- Regulatory Reporting
- Standards Body
- Model Laws
- Regulatory Data
- Open Data
website: https://content.naic.org/
---
