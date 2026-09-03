---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 65
  human_in_the_loop: 1
  name: Optimizely Agentic Access
  operation_count: 135
  slug: optimizely-agentic-access
  summary_line: 135 operations · 65 acting · 1 human-in-the-loop
api_count: 37
apis:
- description: Optimizely's hosted remote Model Context Protocol server for Web and Feature Experimentation, on the Opal MCP platform. Tools are prefixed exp_ and cover querying projects/flags/experiments/environmen
  name: Optimizely Remote MCP Server — Experimentation
  slug: mcp-experimentation
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage campaign assets such as images and media files.
  name: Optimizely Assets API
  slug: optimizely-assets-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage custom attributes used for audience targeting and segmentation.
  name: Optimizely Attributes API
  slug: optimizely-attributes-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create and manage audience segments for targeting experiments and rollouts.
  name: Optimizely Audiences API
  slug: optimizely-audiences-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage content campaigns and editorial calendar entries.
  name: Optimizely Campaigns API
  slug: optimizely-campaigns-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage catalog entries including products, variants, packages, and bundles.
  name: Optimizely Catalog Entries API
  slug: optimizely-catalog-entries-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage relationships between catalog entries and nodes.
  name: Optimizely Catalog Entry Relations API
  slug: optimizely-catalog-entry-relations-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage catalog nodes (categories) for organizing entries.
  name: Optimizely Catalog Nodes API
  slug: optimizely-catalog-nodes-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage product catalogs that organize commerce content.
  name: Optimizely Catalogs API
  slug: optimizely-catalogs-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage content items including articles and other content types within the CMP content repository.
  name: Optimizely Content API
  slug: optimizely-content-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Retrieve available content type definitions.
  name: Optimizely Content Types API
  slug: optimizely-content-types-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage customer accounts and contact information.
  name: Optimizely Customers API
  slug: optimizely-customers-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage environments within a project for developing, staging, and deploying flag configurations.
  name: Optimizely Environments API
  slug: optimizely-environments-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Send customer events to ODP for tracking actions, behaviors, and interactions across channels.
  name: Optimizely Events API
  slug: optimizely-events-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create and manage A/B test experiments on top of feature flags.
  name: Optimizely Experiments API
  slug: optimizely-experiments-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage reusable extensions that encapsulate experiment logic and visual changes.
  name: Optimizely Extensions API
  slug: optimizely-extensions-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage features with variables used in feature flag configurations.
  name: Optimizely Features API
  slug: optimizely-features-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create and manage feature flags with variables and variations for controlled rollouts and experimentation.
  name: Optimizely Flags API
  slug: optimizely-flags-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Execute GraphQL queries against the Optimizely content graph to retrieve and search content.
  name: Optimizely GraphQL API
  slug: optimizely-graphql-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage labels used for categorizing and organizing content.
  name: Optimizely Labels API
  slug: optimizely-labels-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage mailing lists used for campaign distribution.
  name: Optimizely Mailing Lists API
  slug: optimizely-mailing-lists-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create, update, and manage objects such as products, orders, and custom entities in ODP.
  name: Optimizely Objects API
  slug: optimizely-objects-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage purchase orders, cart operations, and order workflows.
  name: Optimizely Orders API
  slug: optimizely-orders-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage page definitions that specify which URLs or conditions trigger experiments.
  name: Optimizely Pages API
  slug: optimizely-pages-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create, update, and retrieve customer profiles with unified identity resolution.
  name: Optimizely Profiles API
  slug: optimizely-profiles-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage Feature Experimentation projects that serve as containers for flags, experiments, and environments.
  name: Optimizely Projects API
  slug: optimizely-projects-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage recipients and recipient lists for email campaigns.
  name: Optimizely Recipients API
  slug: optimizely-recipients-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage rulesets that define which variation a flag delivers to visitors within a given environment.
  name: Optimizely Rulesets API
  slug: optimizely-rulesets-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage the ODP schema including domain objects and their fields.
  name: Optimizely Schema API
  slug: optimizely-schema-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Query customer segments and audience definitions.
  name: Optimizely Segments API
  slug: optimizely-segments-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Retrieve site definitions including language settings and configuration.
  name: Optimizely Sites API
  slug: optimizely-sites-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage smart campaigns that automate multi-step marketing workflows.
  name: Optimizely Smart Campaigns API
  slug: optimizely-smart-campaigns-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage content tasks, assignments, and workflow steps within the content marketing platform.
  name: Optimizely Tasks API
  slug: optimizely-tasks-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Send transactional emails triggered by recipient actions or events.
  name: Optimizely Transactional Mail API
  slug: optimizely-transactional-mail-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage unsubscribe lists for opt-out recipients.
  name: Optimizely Unsubscribes API
  slug: optimizely-unsubscribes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Accounts API from Optimizely — 7 operation(s) for accounts.
  name: Optimizely Accounts API
  slug: optimizely-accounts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Activate API from Optimizely — 1 operation(s) for activate.
  name: Optimizely Activate API
  slug: optimizely-activate-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin Action Configurations API from Optimizely — 6 operation(s) for admin action configurations.
  name: Optimizely Admin Action Configurations API
  slug: optimizely-admin-action-configurations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin Action Permissions API from Optimizely — 5 operation(s) for admin action permissions.
  name: Optimizely Admin Action Permissions API
  slug: optimizely-admin-action-permissions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin User Profile Passwords API from Optimizely — 5 operation(s) for admin user profile passwords.
  name: Optimizely Admin User Profile Passwords API
  slug: optimizely-admin-user-profile-passwords-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin User Profile Preferences API from Optimizely — 7 operation(s) for admin user profile preferences.
  name: Optimizely Admin User Profile Preferences API
  slug: optimizely-admin-user-profile-preferences-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin User Profile Websites API from Optimizely — 5 operation(s) for admin user profile websites.
  name: Optimizely Admin User Profile Websites API
  slug: optimizely-admin-user-profile-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin User Profiles API from Optimizely — 12 operation(s) for admin user profiles.
  name: Optimizely Admin User Profiles API
  slug: optimizely-admin-user-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Adyen API from Optimizely — 1 operation(s) for adyen.
  name: Optimizely Adyen API
  slug: optimizely-adyen-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Affiliates API from Optimizely — 7 operation(s) for affiliates.
  name: Optimizely Affiliates API
  slug: optimizely-affiliates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Log Endpoint
  name: Optimizely API Reference API
  slug: optimizely-api-reference-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Applepay API from Optimizely — 2 operation(s) for applepay.
  name: Optimizely Applepay API
  slug: optimizely-applepay-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Application Es Logs API from Optimizely — 2 operation(s) for application es logs.
  name: Optimizely Application Es Logs API
  slug: optimizely-application-es-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Application Logs API from Optimizely — 5 operation(s) for application logs.
  name: Optimizely Application Logs API
  slug: optimizely-application-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Application Messages API from Optimizely — 5 operation(s) for application messages.
  name: Optimizely Application Messages API
  slug: optimizely-application-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage email attachments
  name: Optimizely Attachments API
  slug: optimizely-attachments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Attribute Types API from Optimizely — 9 operation(s) for attribute types.
  name: Optimizely Attribute Types API
  slug: optimizely-attribute-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Attribute Values API from Optimizely — 11 operation(s) for attribute values.
  name: Optimizely Attribute Values API
  slug: optimizely-attribute-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get a list of bucketing decisions for a visitor.
  name: Optimizely Attribution API
  slug: optimizely-attribution-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Audits API from Optimizely — 5 operation(s) for audits.
  name: Optimizely Audits API
  slug: optimizely-audits-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Autocomplete API from Optimizely — 2 operation(s) for autocomplete.
  name: Optimizely Autocomplete API
  slug: optimizely-autocomplete-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Available Languages API from Optimizely — 1 operation(s) for available languages.
  name: Optimizely Available Languages API
  slug: optimizely-available-languages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Badge Attribute Values API from Optimizely — 5 operation(s) for badge attribute values.
  name: Optimizely Badge Attribute Values API
  slug: optimizely-badge-attribute-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Badge Products API from Optimizely — 5 operation(s) for badge products.
  name: Optimizely Badge Products API
  slug: optimizely-badge-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Badges API from Optimizely — 7 operation(s) for badges.
  name: Optimizely Badges API
  slug: optimizely-badges-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Batch API from Optimizely — 1 operation(s) for batch.
  name: Optimizely Batch API
  slug: optimizely-batch-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Create and send messages as batches to recipients segmented in separate platform
  name: Optimizely Batch sending API
  slug: optimizely-batch-sending-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 🏆 BestBets API from Optimizely — 2 operation(s) for 🏆 bestbets.
  name: Optimizely 🏆 BestBets API
  slug: optimizely-bestbets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Bill To Address Fields API from Optimizely — 5 operation(s) for bill to address fields.
  name: Optimizely Bill To Address Fields API
  slug: optimizely-bill-to-address-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Billtos API from Optimizely — 4 operation(s) for billtos.
  name: Optimizely Billtos API
  slug: optimizely-billtos-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Blob Storage Containers API from Optimizely — 2 operation(s) for blob storage containers.
  name: Optimizely Blob Storage Containers API
  slug: optimizely-blob-storage-containers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage recipients on the blocklist
  name: Optimizely Blocklist entries API
  slug: optimizely-blocklist-entries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Brand Category Images API from Optimizely — 6 operation(s) for brand category images.
  name: Optimizely Brand Category Images API
  slug: optimizely-brand-category-images-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Brand Compliance API from Optimizely — 2 operation(s) for brand compliance.
  name: Optimizely Brand Compliance API
  slug: optimizely-brand-compliance-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Brandalphabet API from Optimizely — 1 operation(s) for brandalphabet.
  name: Optimizely Brandalphabet API
  slug: optimizely-brandalphabet-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Brands API from Optimizely — 23 operation(s) for brands.
  name: Optimizely Brands API
  slug: optimizely-brands-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Budget Calendars API from Optimizely — 5 operation(s) for budget calendars.
  name: Optimizely Budget Calendars API
  slug: optimizely-budget-calendars-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Budgetcalendars API from Optimizely — 2 operation(s) for budgetcalendars.
  name: Optimizely Budgetcalendars API
  slug: optimizely-budgetcalendars-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Budgets API from Optimizely — 2 operation(s) for budgets.
  name: Optimizely Budgets API
  slug: optimizely-budgets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carrier Packages API from Optimizely — 7 operation(s) for carrier packages.
  name: Optimizely Carrier Packages API
  slug: optimizely-carrier-packages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carrier Zone Postal Code Ranges API from Optimizely — 5 operation(s) for carrier zone postal code ranges.
  name: Optimizely Carrier Zone Postal Code Ranges API
  slug: optimizely-carrier-zone-postal-code-ranges-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carrier Zone Rates API from Optimizely — 5 operation(s) for carrier zone rates.
  name: Optimizely Carrier Zone Rates API
  slug: optimizely-carrier-zone-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carrier Zones API from Optimizely — 7 operation(s) for carrier zones.
  name: Optimizely Carrier Zones API
  slug: optimizely-carrier-zones-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carriers API from Optimizely — 12 operation(s) for carriers.
  name: Optimizely Carriers API
  slug: optimizely-carriers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carts API from Optimizely — 8 operation(s) for carts.
  name: Optimizely Carts API
  slug: optimizely-carts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Catalogpages API from Optimizely — 1 operation(s) for catalogpages.
  name: Optimizely Catalogpages API
  slug: optimizely-catalogpages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Categories API from Optimizely — 22 operation(s) for categories.
  name: Optimizely Categories API
  slug: optimizely-categories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Attribute Types API from Optimizely — 7 operation(s) for category attribute types.
  name: Optimizely Category Attribute Types API
  slug: optimizely-category-attribute-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Attribute Values API from Optimizely — 5 operation(s) for category attribute values.
  name: Optimizely Category Attribute Values API
  slug: optimizely-category-attribute-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Persona Extendeds API from Optimizely — 5 operation(s) for category persona extendeds.
  name: Optimizely Category Persona Extendeds API
  slug: optimizely-category-persona-extendeds-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Personas API from Optimizely — 5 operation(s) for category personas.
  name: Optimizely Category Personas API
  slug: optimizely-category-personas-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Products API from Optimizely — 5 operation(s) for category products.
  name: Optimizely Category Products API
  slug: optimizely-category-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Related Products API from Optimizely — 5 operation(s) for category related products.
  name: Optimizely Category Related Products API
  slug: optimizely-category-related-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Tax Exemptions API from Optimizely — 5 operation(s) for category tax exemptions.
  name: Optimizely Category Tax Exemptions API
  slug: optimizely-category-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with approval of flag changes
  name: Optimizely Change Approvals API
  slug: optimizely-change-approvals-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get a list of changes by project.
  name: Optimizely Change History API
  slug: optimizely-change-history-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Changes API from Optimizely — 1 operation(s) for changes.
  name: Optimizely Changes API
  slug: optimizely-changes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Checks API from Optimizely — 2 operation(s) for checks.
  name: Optimizely Checks API
  slug: optimizely-checks-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage click profiles
  name: Optimizely Click profiles API
  slug: optimizely-click-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Collaborators API from Optimizely — 2 operation(s) for collaborators.
  name: Optimizely Collaborators API
  slug: optimizely-collaborators-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Compliance API from Optimizely — 7 operation(s) for compliance.
  name: Optimizely Compliance API
  slug: optimizely-compliance-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Config API from Optimizely — 1 operation(s) for config.
  name: Optimizely Config API
  slug: optimizely-config-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage registration confirmations (opt-in emails)
  name: Optimizely Confirmations API
  slug: optimizely-confirmations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Consent API from Optimizely — 2 operation(s) for consent.
  name: Optimizely Consent API
  slug: optimizely-consent-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The legacy Consent API is only available for the United States region. Migrate to the latest Update consent API.
  name: Optimizely Consent (Legacy) API
  slug: optimizely-consent-legacy-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Content Item Fields API from Optimizely — 5 operation(s) for content item fields.
  name: Optimizely Content Item Fields API
  slug: optimizely-content-item-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Content Items API from Optimizely — 5 operation(s) for content items.
  name: Optimizely Content Items API
  slug: optimizely-content-items-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Content Managers API from Optimizely — 6 operation(s) for content managers.
  name: Optimizely Content Managers API
  slug: optimizely-content-managers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Content Page States API from Optimizely — 5 operation(s) for content page states.
  name: Optimizely Content Page States API
  slug: optimizely-content-page-states-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Contents API from Optimizely — 5 operation(s) for contents.
  name: Optimizely Contents API
  slug: optimizely-contents-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Countries API from Optimizely — 7 operation(s) for countries.
  name: Optimizely Countries API
  slug: optimizely-countries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Country Vat Rates API from Optimizely — 5 operation(s) for country vat rates.
  name: Optimizely Country Vat Rates API
  slug: optimizely-country-vat-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage coupon blocks that organize coupon codes
  name: Optimizely Coupon blocks API
  slug: optimizely-coupon-blocks-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Credit Card Transactions API from Optimizely — 5 operation(s) for credit card transactions.
  name: Optimizely Credit Card Transactions API
  slug: optimizely-credit-card-transactions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Criteria Types API from Optimizely — 1 operation(s) for criteria types.
  name: Optimizely Criteria Types API
  slug: optimizely-criteria-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Currencies API from Optimizely — 7 operation(s) for currencies.
  name: Optimizely Currencies API
  slug: optimizely-currencies-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Currency Rates API from Optimizely — 5 operation(s) for currency rates.
  name: Optimizely Currency Rates API
  slug: optimizely-currency-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage custom blocklists
  name: Optimizely Custom blocklists API
  slug: optimizely-custom-blocklists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to manage Custom Field definitions for organizing and annotating flags
  name: Optimizely Custom Fields API
  slug: optimizely-custom-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Custom Properties API from Optimizely — 6 operation(s) for custom properties.
  name: Optimizely Custom Properties API
  slug: optimizely-custom-properties-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Budgets API from Optimizely — 5 operation(s) for customer budgets.
  name: Optimizely Customer Budgets API
  slug: optimizely-customer-budgets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Carriers API from Optimizely — 5 operation(s) for customer carriers.
  name: Optimizely Customer Carriers API
  slug: optimizely-customer-carriers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Cost Codes API from Optimizely — 7 operation(s) for customer cost codes.
  name: Optimizely Customer Cost Codes API
  slug: optimizely-customer-cost-codes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Order Changes API from Optimizely — 5 operation(s) for customer order changes.
  name: Optimizely Customer Order Changes API
  slug: optimizely-customer-order-changes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Order Gift Cards API from Optimizely — 5 operation(s) for customer order gift cards.
  name: Optimizely Customer Order Gift Cards API
  slug: optimizely-customer-order-gift-cards-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Order Promotions API from Optimizely — 5 operation(s) for customer order promotions.
  name: Optimizely Customer Order Promotions API
  slug: optimizely-customer-order-promotions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Order Taxes API from Optimizely — 5 operation(s) for customer order taxes.
  name: Optimizely Customer Order Taxes API
  slug: optimizely-customer-order-taxes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Orders API from Optimizely — 14 operation(s) for customer orders.
  name: Optimizely Customer Orders API
  slug: optimizely-customer-orders-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Product Set Products API from Optimizely — 5 operation(s) for customer product set products.
  name: Optimizely Customer Product Set Products API
  slug: optimizely-customer-product-set-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Product Sets API from Optimizely — 8 operation(s) for customer product sets.
  name: Optimizely Customer Product Sets API
  slug: optimizely-customer-product-sets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Product Visibility Additions API from Optimizely — 5 operation(s) for customer product visibility additions.
  name: Optimizely Customer Product Visibility Additions API
  slug: optimizely-customer-product-visibility-additions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Product Visibility Exceptions API from Optimizely — 5 operation(s) for customer product visibility exceptions.
  name: Optimizely Customer Product Visibility Exceptions API
  slug: optimizely-customer-product-visibility-exceptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Products API from Optimizely — 5 operation(s) for customer products.
  name: Optimizely Customer Products API
  slug: optimizely-customer-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer User Profiles API from Optimizely — 5 operation(s) for customer user profiles.
  name: Optimizely Customer User Profiles API
  slug: optimizely-customer-user-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dashboard Panel Positions API from Optimizely — 5 operation(s) for dashboard panel positions.
  name: Optimizely Dashboard Panel Positions API
  slug: optimizely-dashboard-panel-positions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dashboardpanels API from Optimizely — 1 operation(s) for dashboardpanels.
  name: Optimizely Dashboardpanels API
  slug: optimizely-dashboardpanels-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Data Generation API from Optimizely — 1 operation(s) for data generation.
  name: Optimizely Data Generation API
  slug: optimizely-data-generation-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Database Scripts API from Optimizely — 5 operation(s) for database scripts.
  name: Optimizely Database Scripts API
  slug: optimizely-database-scripts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The DatabaseExports API from Optimizely — 2 operation(s) for databaseexports.
  name: Optimizely Database Exports API
  slug: optimizely-databaseexports-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Datafile API from Optimizely — 1 operation(s) for datafile.
  name: Optimizely Datafile API
  slug: optimizely-datafile-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dealer Categories API from Optimizely — 5 operation(s) for dealer categories.
  name: Optimizely Dealer Categories API
  slug: optimizely-dealer-categories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dealer Products API from Optimizely — 5 operation(s) for dealer products.
  name: Optimizely Dealer Products API
  slug: optimizely-dealer-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dealers API from Optimizely — 11 operation(s) for dealers.
  name: Optimizely Dealers API
  slug: optimizely-dealers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Decide API from Optimizely — 1 operation(s) for decide.
  name: Optimizely Decide API
  slug: optimizely-decide-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 📖 Definition ( v2 ) API from Optimizely — 2 operation(s) for 📖 definition ( v2 ).
  name: Optimizely 📖 Definition ( v2 ) API
  slug: optimizely-definition-v2-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 📖 Definition ( v3 ) API from Optimizely — 2 operation(s) for 📖 definition ( v3 ).
  name: Optimizely 📖 Definition ( v3 ) API
  slug: optimizely-definition-v3-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Delivery management operations
  name: Optimizely Deliveries API
  slug: optimizely-deliveries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Deployments API from Optimizely — 5 operation(s) for deployments.
  name: Optimizely Deployments API
  slug: optimizely-deployments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Device Tokens API from Optimizely — 7 operation(s) for device tokens.
  name: Optimizely Device Tokens API
  slug: optimizely-device-tokens-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Documents API from Optimizely — 5 operation(s) for documents.
  name: Optimizely Documents API
  slug: optimizely-documents-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email API from Optimizely — 3 operation(s) for email.
  name: Optimizely Email API
  slug: optimizely-email-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Lists API from Optimizely — 7 operation(s) for email lists.
  name: Optimizely Email Lists API
  slug: optimizely-email-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Message Addresses API from Optimizely — 5 operation(s) for email message addresses.
  name: Optimizely Email Message Addresses API
  slug: optimizely-email-message-addresses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Message Attachments API from Optimizely — 5 operation(s) for email message attachments.
  name: Optimizely Email Message Attachments API
  slug: optimizely-email-message-attachments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Message Delivery Attempts API from Optimizely — 5 operation(s) for email message delivery attempts.
  name: Optimizely Email Message Delivery Attempts API
  slug: optimizely-email-message-delivery-attempts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Messages API from Optimizely — 8 operation(s) for email messages.
  name: Optimizely Email Messages API
  slug: optimizely-email-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Subscriber Email Lists API from Optimizely — 5 operation(s) for email subscriber email lists.
  name: Optimizely Email Subscriber Email Lists API
  slug: optimizely-email-subscriber-email-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Subscribers API from Optimizely — 6 operation(s) for email subscribers.
  name: Optimizely Email Subscribers API
  slug: optimizely-email-subscribers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Templates API from Optimizely — 10 operation(s) for email templates.
  name: Optimizely Email Templates API
  slug: optimizely-email-templates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The EmailAttachments API from Optimizely — 1 operation(s) for emailattachments.
  name: Optimizely Email Attachments API
  slug: optimizely-emailattachments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Entity API from Optimizely — 3 operation(s) for entity.
  name: Optimizely Entity API
  slug: optimizely-entity-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Entity Configurations API from Optimizely — 7 operation(s) for entity configurations.
  name: Optimizely Entity Configurations API
  slug: optimizely-entity-configurations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Entity Definitions API from Optimizely — 6 operation(s) for entity definitions.
  name: Optimizely Entity Definitions API
  slug: optimizely-entity-definitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Entity Permissions API from Optimizely — 5 operation(s) for entity permissions.
  name: Optimizely Entity Permissions API
  slug: optimizely-entity-permissions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Experiment Participants API from Optimizely — 7 operation(s) for experiment participants.
  name: Optimizely Experiment Participants API
  slug: optimizely-experiment-participants-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The ExperimentSummary API from Optimizely — 1 operation(s) for experimentsummary.
  name: Optimizely Experiment Summary API
  slug: optimizely-experimentsummary-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get credentials to access experimentation events export data.
  name: Optimizely Export Credentials API
  slug: optimizely-export-credentials-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Exports API from Optimizely — 4 operation(s) for exports.
  name: Optimizely Exports API
  slug: optimizely-exports-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Feederdata API from Optimizely — 6 operation(s) for feederdata.
  name: Optimizely Feederdata API
  slug: optimizely-feederdata-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Fields API from Optimizely — 4 operation(s) for fields.
  name: Optimizely Fields API
  slug: optimizely-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Fields schema API from Optimizely — 2 operation(s) for fields schema.
  name: Optimizely Fields schema API
  slug: optimizely-fields-schema-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage folders for mailings, message templates, custom blacklists, images, recipient list and attachment
  name: Optimizely Folders API
  slug: optimizely-folders-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Forms API from Optimizely — 2 operation(s) for forms.
  name: Optimizely Forms API
  slug: optimizely-forms-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Gift Card Transactions API from Optimizely — 5 operation(s) for gift card transactions.
  name: Optimizely Gift Card Transactions API
  slug: optimizely-gift-card-transactions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Gift Cards API from Optimizely — 9 operation(s) for gift cards.
  name: Optimizely Gift Cards API
  slug: optimizely-gift-cards-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Global Synonyms API from Optimizely — 5 operation(s) for global synonyms.
  name: Optimizely Global Synonyms API
  slug: optimizely-global-synonyms-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Googlepay API from Optimizely — 1 operation(s) for googlepay.
  name: Optimizely Googlepay API
  slug: optimizely-googlepay-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with mutual exclusion groups
  name: Optimizely Groups API
  slug: optimizely-groups-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Holdouts API from Optimizely — 4 operation(s) for holdouts.
  name: Optimizely Holdouts API
  slug: optimizely-holdouts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Html Redirects API from Optimizely — 5 operation(s) for html redirects.
  name: Optimizely Html Redirects API
  slug: optimizely-html-redirects-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Identifiers API from Optimizely — 3 operation(s) for identifiers.
  name: Optimizely Identifiers API
  slug: optimizely-identifiers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Impressions Usage API from Optimizely — 2 operation(s) for impressions usage.
  name: Optimizely Impressions Usage API
  slug: optimizely-impressions-usage-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Connections API from Optimizely — 5 operation(s) for integration connections.
  name: Optimizely Integration Connections API
  slug: optimizely-integration-connections-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Job Es Logs API from Optimizely — 2 operation(s) for integration job es logs.
  name: Optimizely Integration Job Es Logs API
  slug: optimizely-integration-job-es-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Job Logs API from Optimizely — 5 operation(s) for integration job logs.
  name: Optimizely Integration Job Logs API
  slug: optimizely-integration-job-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Job Parameters API from Optimizely — 5 operation(s) for integration job parameters.
  name: Optimizely Integration Job Parameters API
  slug: optimizely-integration-job-parameters-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Jobs API from Optimizely — 7 operation(s) for integration jobs.
  name: Optimizely Integration Jobs API
  slug: optimizely-integration-jobs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Invoice Histories API from Optimizely — 7 operation(s) for invoice histories.
  name: Optimizely Invoice Histories API
  slug: optimizely-invoice-histories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Invoice History Lines API from Optimizely — 5 operation(s) for invoice history lines.
  name: Optimizely Invoice History Lines API
  slug: optimizely-invoice-history-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Invoice History Taxes API from Optimizely — 5 operation(s) for invoice history taxes.
  name: Optimizely Invoice History Taxes API
  slug: optimizely-invoice-history-taxes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Invoices API from Optimizely — 3 operation(s) for invoices.
  name: Optimizely Invoices API
  slug: optimizely-invoices-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definition Parameters API from Optimizely — 5 operation(s) for job definition parameters.
  name: Optimizely Job Definition Parameters API
  slug: optimizely-job-definition-parameters-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definition Step Field Maps API from Optimizely — 5 operation(s) for job definition step field maps.
  name: Optimizely Job Definition Step Field Maps API
  slug: optimizely-job-definition-step-field-maps-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definition Step Parameters API from Optimizely — 5 operation(s) for job definition step parameters.
  name: Optimizely Job Definition Step Parameters API
  slug: optimizely-job-definition-step-parameters-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definition Steps API from Optimizely — 7 operation(s) for job definition steps.
  name: Optimizely Job Definition Steps API
  slug: optimizely-job-definition-steps-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definitions API from Optimizely — 8 operation(s) for job definitions.
  name: Optimizely Job Definitions API
  slug: optimizely-job-definitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Jobquotes API from Optimizely — 2 operation(s) for jobquotes.
  name: Optimizely Jobquotes API
  slug: optimizely-jobquotes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Languages API from Optimizely — 6 operation(s) for languages.
  name: Optimizely Languages API
  slug: optimizely-languages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Library API from Optimizely — 24 operation(s) for library.
  name: Optimizely Library API
  slug: optimizely-library-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: 'A List Attribute is a set of user identifiers that you have uploaded to Optimizely. Membership in a list can be used to define an Optimizely audience, so you can target experiments and campaigns only '
  name: Optimizely List Attributes API
  slug: optimizely-list-attributes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Lists API from Optimizely — 2 operation(s) for lists.
  name: Optimizely Lists API
  slug: optimizely-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Local Tax Rate Tax Exemptions API from Optimizely — 5 operation(s) for local tax rate tax exemptions.
  name: Optimizely Local Tax Rate Tax Exemptions API
  slug: optimizely-local-tax-rate-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Local Tax Rates API from Optimizely — 6 operation(s) for local tax rates.
  name: Optimizely Local Tax Rates API
  slug: optimizely-local-tax-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 📜 Logs API from Optimizely — 1 operation(s) for 📜 logs.
  name: Optimizely 📜 Logs API
  slug: optimizely-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Lookup API from Optimizely — 1 operation(s) for lookup.
  name: Optimizely Lookup API
  slug: optimizely-lookup-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get archived mailings
  name: Optimizely Mail archive API
  slug: optimizely-mail-archive-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get information about a mail ID
  name: Optimizely Mail ID API
  slug: optimizely-mail-id-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Message Audits API from Optimizely — 5 operation(s) for message audits.
  name: Optimizely Message Audits API
  slug: optimizely-message-audits-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Message Statuses API from Optimizely — 5 operation(s) for message statuses.
  name: Optimizely Message Statuses API
  slug: optimizely-message-statuses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Message Targets API from Optimizely — 5 operation(s) for message targets.
  name: Optimizely Message Targets API
  slug: optimizely-message-targets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage message templates
  name: Optimizely Message templates API
  slug: optimizely-message-templates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Messages API from Optimizely — 11 operation(s) for messages.
  name: Optimizely Messages API
  slug: optimizely-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Milestones API from Optimizely — 2 operation(s) for milestones.
  name: Optimizely Milestones API
  slug: optimizely-milestones-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Mobilecontent API from Optimizely — 1 operation(s) for mobilecontent.
  name: Optimizely Mobilecontent API
  slug: optimizely-mobilecontent-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Mobius Themes API from Optimizely — 5 operation(s) for mobius themes.
  name: Optimizely Mobius Themes API
  slug: optimizely-mobius-themes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Nodes API from Optimizely — 6 operation(s) for nodes.
  name: Optimizely Nodes API
  slug: optimizely-nodes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Oauth API from Optimizely — 1 operation(s) for oauth.
  name: Optimizely OAUTH API
  slug: optimizely-oauth-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Object schema API from Optimizely — 2 operation(s) for object schema.
  name: Optimizely Object schema API
  slug: optimizely-object-schema-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Odpimport API from Optimizely — 1 operation(s) for odpimport.
  name: Optimizely Odpimport API
  slug: optimizely-odpimport-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 🔒 OIDC API from Optimizely — 1 operation(s) for 🔒 oidc.
  name: Optimizely 🔒 OIDC API
  slug: optimizely-oidc-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: View, update and create opt-in processes
  name: Optimizely Opt-in processes API
  slug: optimizely-opt-in-processes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Optimizely Edge Decider API from Optimizely — 1 operation(s) for optimizely edge decider.
  name: Optimizely Optimizely Edge Decider API
  slug: optimizely-optimizely-edge-decider-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Histories API from Optimizely — 8 operation(s) for order histories.
  name: Optimizely Order Histories API
  slug: optimizely-order-histories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order History Lines API from Optimizely — 5 operation(s) for order history lines.
  name: Optimizely Order History Lines API
  slug: optimizely-order-history-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order History Promotions API from Optimizely — 5 operation(s) for order history promotions.
  name: Optimizely Order History Promotions API
  slug: optimizely-order-history-promotions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order History Taxes API from Optimizely — 5 operation(s) for order history taxes.
  name: Optimizely Order History Taxes API
  slug: optimizely-order-history-taxes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Line Requisitions API from Optimizely — 5 operation(s) for order line requisitions.
  name: Optimizely Order Line Requisitions API
  slug: optimizely-order-line-requisitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Line Rfqs API from Optimizely — 5 operation(s) for order line rfqs.
  name: Optimizely Order Line Rfqs API
  slug: optimizely-order-line-rfqs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Line Vats API from Optimizely — 5 operation(s) for order line vats.
  name: Optimizely Order Line Vats API
  slug: optimizely-order-line-vats-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Lines API from Optimizely — 6 operation(s) for order lines.
  name: Optimizely Order Lines API
  slug: optimizely-order-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Promotion Codes API from Optimizely — 5 operation(s) for order promotion codes.
  name: Optimizely Order Promotion Codes API
  slug: optimizely-order-promotion-codes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Status Mappings API from Optimizely — 5 operation(s) for order status mappings.
  name: Optimizely Order Status Mappings API
  slug: optimizely-order-status-mappings-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Orderapprovals API from Optimizely — 2 operation(s) for orderapprovals.
  name: Optimizely Orderapprovals API
  slug: optimizely-orderapprovals-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Orderfeed API from Optimizely — 1 operation(s) for orderfeed.
  name: Optimizely Orderfeed API
  slug: optimizely-orderfeed-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Orderstatusmappings API from Optimizely — 1 operation(s) for orderstatusmappings.
  name: Optimizely Orderstatusmappings API
  slug: optimizely-orderstatusmappings-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Override API from Optimizely — 1 operation(s) for override.
  name: Optimizely Override API
  slug: optimizely-override-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page State Contexts API from Optimizely — 5 operation(s) for page state contexts.
  name: Optimizely Page State Contexts API
  slug: optimizely-page-state-contexts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page States API from Optimizely — 6 operation(s) for page states.
  name: Optimizely Page States API
  slug: optimizely-page-states-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page Temporaries API from Optimizely — 5 operation(s) for page temporaries.
  name: Optimizely Page Temporaries API
  slug: optimizely-page-temporaries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page Urls API from Optimizely — 5 operation(s) for page urls.
  name: Optimizely Page Urls API
  slug: optimizely-page-urls-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page Versions API from Optimizely — 5 operation(s) for page versions.
  name: Optimizely Page Versions API
  slug: optimizely-page-versions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Payment Methods API from Optimizely — 7 operation(s) for payment methods.
  name: Optimizely Payment Methods API
  slug: optimizely-payment-methods-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Paymentauthentication API from Optimizely — 9 operation(s) for paymentauthentication.
  name: Optimizely Paymentauthentication API
  slug: optimizely-paymentauthentication-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Paymetric API from Optimizely — 2 operation(s) for paymetric.
  name: Optimizely Paymetric API
  slug: optimizely-paymetric-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Persona User Profiles API from Optimizely — 5 operation(s) for persona user profiles.
  name: Optimizely Persona User Profiles API
  slug: optimizely-persona-user-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage personalized email attachments
  name: Optimizely Personalized Attachments API
  slug: optimizely-personalized-attachments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Personas API from Optimizely — 10 operation(s) for personas.
  name: Optimizely Personas API
  slug: optimizely-personas-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 🏆 Pinned Results API from Optimizely — 5 operation(s) for 🏆 pinned results.
  name: Optimizely 🏆 Pinned Results API
  slug: optimizely-pinned-results-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Plan & Usage information for current account
  name: Optimizely Plan API
  slug: optimizely-plan-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Plugins API from Optimizely — 7 operation(s) for plugins.
  name: Optimizely Plugins API
  slug: optimizely-plugins-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Price Matrices API from Optimizely — 7 operation(s) for price matrices.
  name: Optimizely Price Matrices API
  slug: optimizely-price-matrices-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Also Purchased Withs API from Optimizely — 5 operation(s) for product also purchased withs.
  name: Optimizely Product Also Purchased Withs API
  slug: optimizely-product-also-purchased-withs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Attribute Values API from Optimizely — 5 operation(s) for product attribute values.
  name: Optimizely Product Attribute Values API
  slug: optimizely-product-attribute-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Images API from Optimizely — 7 operation(s) for product images.
  name: Optimizely Product Images API
  slug: optimizely-product-images-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Kit Section Options API from Optimizely — 5 operation(s) for product kit section options.
  name: Optimizely Product Kit Section Options API
  slug: optimizely-product-kit-section-options-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Kit Sections API from Optimizely — 6 operation(s) for product kit sections.
  name: Optimizely Product Kit Sections API
  slug: optimizely-product-kit-sections-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Lines API from Optimizely — 6 operation(s) for product lines.
  name: Optimizely Product Lines API
  slug: optimizely-product-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Related Products API from Optimizely — 5 operation(s) for product related products.
  name: Optimizely Product Related Products API
  slug: optimizely-product-related-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Tax Exemptions API from Optimizely — 5 operation(s) for product tax exemptions.
  name: Optimizely Product Tax Exemptions API
  slug: optimizely-product-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Top Sellers API from Optimizely — 5 operation(s) for product top sellers.
  name: Optimizely Product Top Sellers API
  slug: optimizely-product-top-sellers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Unit Of Measures API from Optimizely — 5 operation(s) for product unit of measures.
  name: Optimizely Product Unit Of Measures API
  slug: optimizely-product-unit-of-measures-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Warehouses API from Optimizely — 5 operation(s) for product warehouses.
  name: Optimizely Product Warehouses API
  slug: optimizely-product-warehouses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Products API from Optimizely — 54 operation(s) for products.
  name: Optimizely Products API
  slug: optimizely-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Productsrssfeed API from Optimizely — 1 operation(s) for productsrssfeed.
  name: Optimizely Productsrssfeed API
  slug: optimizely-productsrssfeed-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Promotion Result Products API from Optimizely — 5 operation(s) for promotion result products.
  name: Optimizely Promotion Result Products API
  slug: optimizely-promotion-result-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Promotion Result Types API from Optimizely — 1 operation(s) for promotion result types.
  name: Optimizely Promotion Result Types API
  slug: optimizely-promotion-result-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Promotion Results API from Optimizely — 12 operation(s) for promotion results.
  name: Optimizely Promotion Results API
  slug: optimizely-promotion-results-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Promotions API from Optimizely — 12 operation(s) for promotions.
  name: Optimizely Promotions API
  slug: optimizely-promotions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Property Attribute Configurations API from Optimizely — 5 operation(s) for property attribute configurations.
  name: Optimizely Property Attribute Configurations API
  slug: optimizely-property-attribute-configurations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Property Configurations API from Optimizely — 7 operation(s) for property configurations.
  name: Optimizely Property Configurations API
  slug: optimizely-property-configurations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Property Permissions API from Optimizely — 5 operation(s) for property permissions.
  name: Optimizely Property Permissions API
  slug: optimizely-property-permissions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Publishing API from Optimizely — 4 operation(s) for publishing.
  name: Optimizely Publishing API
  slug: optimizely-publishing-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Customer User Profile Maps API from Optimizely — 5 operation(s) for punch out customer user profile maps.
  name: Optimizely Punch Out Customer User Profile Maps API
  slug: optimizely-punch-out-customer-user-profile-maps-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Request Extrinsics API from Optimizely — 5 operation(s) for punch out order request extrinsics.
  name: Optimizely Punch Out Order Request Extrinsics API
  slug: optimizely-punch-out-order-request-extrinsics-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Request Item Out Extrinsics API from Optimizely — 5 operation(s) for punch out order request item out extrinsics.
  name: Optimizely Punch Out Order Request Item Out Extrinsics API
  slug: optimizely-punch-out-order-request-item-out-extrinsics-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Request Item Outs API from Optimizely — 7 operation(s) for punch out order request item outs.
  name: Optimizely Punch Out Order Request Item Outs API
  slug: optimizely-punch-out-order-request-item-outs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Request Messages API from Optimizely — 5 operation(s) for punch out order request messages.
  name: Optimizely Punch Out Order Request Messages API
  slug: optimizely-punch-out-order-request-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Requests API from Optimizely — 8 operation(s) for punch out order requests.
  name: Optimizely Punch Out Order Requests API
  slug: optimizely-punch-out-order-requests-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Session Accesses API from Optimizely — 5 operation(s) for punch out session accesses.
  name: Optimizely Punch Out Session Accesses API
  slug: optimizely-punch-out-session-accesses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Session Extrinsics API from Optimizely — 5 operation(s) for punch out session extrinsics.
  name: Optimizely Punch Out Session Extrinsics API
  slug: optimizely-punch-out-session-extrinsics-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Session Item Ins API from Optimizely — 5 operation(s) for punch out session item ins.
  name: Optimizely Punch Out Session Item Ins API
  slug: optimizely-punch-out-session-item-ins-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Sessions API from Optimizely — 10 operation(s) for punch out sessions.
  name: Optimizely Punch Out Sessions API
  slug: optimizely-punch-out-sessions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Setup Requests API from Optimizely — 5 operation(s) for punch out setup requests.
  name: Optimizely Punch Out Setup Requests API
  slug: optimizely-punch-out-setup-requests-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punchout API from Optimizely — 5 operation(s) for punchout.
  name: Optimizely Punchout API
  slug: optimizely-punchout-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Push Notification Logs API from Optimizely — 5 operation(s) for push notification logs.
  name: Optimizely Push Notification Logs API
  slug: optimizely-push-notification-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Push Notification Messages API from Optimizely — 6 operation(s) for push notification messages.
  name: Optimizely Push Notification Messages API
  slug: optimizely-push-notification-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The ▶️ Query ( GraphQL ) API from Optimizely — 1 operation(s) for ▶️ query ( graphql ).
  name: Optimizely ▶️ Query ( GraphQL ) API
  slug: optimizely-query-graphql-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Quotes API from Optimizely — 4 operation(s) for quotes.
  name: Optimizely Quotes API
  slug: optimizely-quotes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rating Services API from Optimizely — 1 operation(s) for rating services.
  name: Optimizely Rating Services API
  slug: optimizely-rating-services-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Reachability API from Optimizely — 2 operation(s) for reachability.
  name: Optimizely Reachability API
  slug: optimizely-reachability-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Realtimecartinventory API from Optimizely — 1 operation(s) for realtimecartinventory.
  name: Optimizely Realtimecartinventory API
  slug: optimizely-realtimecartinventory-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Realtimeinventory API from Optimizely — 1 operation(s) for realtimeinventory.
  name: Optimizely Realtimeinventory API
  slug: optimizely-realtimeinventory-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Realtimepricing API from Optimizely — 1 operation(s) for realtimepricing.
  name: Optimizely Realtimepricing API
  slug: optimizely-realtimepricing-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The RealtimeSegments API from Optimizely — 3 operation(s) for realtimesegments.
  name: Optimizely Realtime Segments API
  slug: optimizely-realtimesegments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: View, copy and update recipient lists
  name: Optimizely Recipient lists API
  slug: optimizely-recipient-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Recommendations API from Optimizely — 5 operation(s) for recommendations.
  name: Optimizely Recommendations API
  slug: optimizely-recommendations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Relationships schema API from Optimizely — 2 operation(s) for relationships schema.
  name: Optimizely Relationships schema API
  slug: optimizely-relationships-schema-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Reports
  name: Optimizely Reports API
  slug: optimizely-reports-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Requisitions API from Optimizely — 4 operation(s) for requisitions.
  name: Optimizely Requisitions API
  slug: optimizely-requisitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 📝 Resources API from Optimizely — 2 operation(s) for 📝 resources.
  name: Optimizely 📝 Resources API
  slug: optimizely-resources-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage mailing responses, such as hard or soft bounces
  name: Optimizely Responses API
  slug: optimizely-responses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Customer Additions API from Optimizely — 5 operation(s) for restriction group customer additions.
  name: Optimizely Restriction Group Customer Additions API
  slug: optimizely-restriction-group-customer-additions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Customer Exceptions API from Optimizely — 5 operation(s) for restriction group customer exceptions.
  name: Optimizely Restriction Group Customer Exceptions API
  slug: optimizely-restriction-group-customer-exceptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Customers API from Optimizely — 5 operation(s) for restriction group customers.
  name: Optimizely Restriction Group Customers API
  slug: optimizely-restriction-group-customers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Product Additions API from Optimizely — 5 operation(s) for restriction group product additions.
  name: Optimizely Restriction Group Product Additions API
  slug: optimizely-restriction-group-product-additions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Product Exceptions API from Optimizely — 5 operation(s) for restriction group product exceptions.
  name: Optimizely Restriction Group Product Exceptions API
  slug: optimizely-restriction-group-product-exceptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Products API from Optimizely — 5 operation(s) for restriction group products.
  name: Optimizely Restriction Group Products API
  slug: optimizely-restriction-group-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Websites API from Optimizely — 5 operation(s) for restriction group websites.
  name: Optimizely Restriction Group Websites API
  slug: optimizely-restriction-group-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Groups API from Optimizely — 12 operation(s) for restriction groups.
  name: Optimizely Restriction Groups API
  slug: optimizely-restriction-groups-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Roles API from Optimizely — 1 operation(s) for roles.
  name: Optimizely Roles API
  slug: optimizely-roles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Clause Customers API from Optimizely — 5 operation(s) for rule clause customers.
  name: Optimizely Rule Clause Customers API
  slug: optimizely-rule-clause-customers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Clause Products API from Optimizely — 5 operation(s) for rule clause products.
  name: Optimizely Rule Clause Products API
  slug: optimizely-rule-clause-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Clauses API from Optimizely — 15 operation(s) for rule clauses.
  name: Optimizely Rule Clauses API
  slug: optimizely-rule-clauses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Managers API from Optimizely — 8 operation(s) for rule managers.
  name: Optimizely Rule Managers API
  slug: optimizely-rule-managers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Type Options API from Optimizely — 5 operation(s) for rule type options.
  name: Optimizely Rule Type Options API
  slug: optimizely-rule-type-options-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Types API from Optimizely — 6 operation(s) for rule types.
  name: Optimizely Rule Types API
  slug: optimizely-rule-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Rules
  name: Optimizely Rules API
  slug: optimizely-rules-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Salespersons API from Optimizely — 7 operation(s) for salespersons.
  name: Optimizely Salespersons API
  slug: optimizely-salespersons-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Save API from Optimizely — 1 operation(s) for save.
  name: Optimizely Save API
  slug: optimizely-save-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Scheduled Change of a flag in an environment
  name: Optimizely Scheduled Change API
  slug: optimizely-scheduled-change-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Scheduled Change of a flag
  name: Optimizely Scheduled Changes API
  slug: optimizely-scheduled-changes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get information about scheduled jobs
  name: Optimizely Scheduled jobs API
  slug: optimizely-scheduled-jobs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search API from Optimizely — 2 operation(s) for search.
  name: Optimizely Search API
  slug: optimizely-search-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Boost Analyzers API from Optimizely — 1 operation(s) for search boost analyzers.
  name: Optimizely Search Boost Analyzers API
  slug: optimizely-search-boost-analyzers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Boosts API from Optimizely — 5 operation(s) for search boosts.
  name: Optimizely Search Boosts API
  slug: optimizely-search-boosts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Stopwords API from Optimizely — 5 operation(s) for search stopwords.
  name: Optimizely Search Stopwords API
  slug: optimizely-search-stopwords-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Synonyms API from Optimizely — 5 operation(s) for search synonyms.
  name: Optimizely Search Synonyms API
  slug: optimizely-search-synonyms-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Term Redirects API from Optimizely — 7 operation(s) for search term redirects.
  name: Optimizely Search Term Redirects API
  slug: optimizely-search-term-redirects-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Section management operations
  name: Optimizely Sections API
  slug: optimizely-sections-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Send Odp Event API from Optimizely — 1 operation(s) for send odp event.
  name: Optimizely Send Odp Event API
  slug: optimizely-send-odp-event-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Sessions API from Optimizely — 3 operation(s) for sessions.
  name: Optimizely Sessions API
  slug: optimizely-sessions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Settings API from Optimizely — 9 operation(s) for settings.
  name: Optimizely Settings API
  slug: optimizely-settings-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship Charges API from Optimizely — 5 operation(s) for ship charges.
  name: Optimizely Ship Charges API
  slug: optimizely-ship-charges-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship Rates API from Optimizely — 5 operation(s) for ship rates.
  name: Optimizely Ship Rates API
  slug: optimizely-ship-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship Rules API from Optimizely — 5 operation(s) for ship rules.
  name: Optimizely Ship Rules API
  slug: optimizely-ship-rules-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship To Address Fields API from Optimizely — 5 operation(s) for ship to address fields.
  name: Optimizely Ship To Address Fields API
  slug: optimizely-ship-to-address-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship Vias API from Optimizely — 11 operation(s) for ship vias.
  name: Optimizely Ship Vias API
  slug: optimizely-ship-vias-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Shipment Package Lines API from Optimizely — 5 operation(s) for shipment package lines.
  name: Optimizely Shipment Package Lines API
  slug: optimizely-shipment-package-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Shipment Packages API from Optimizely — 6 operation(s) for shipment packages.
  name: Optimizely Shipment Packages API
  slug: optimizely-shipment-packages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Shipments API from Optimizely — 6 operation(s) for shipments.
  name: Optimizely Shipments API
  slug: optimizely-shipments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Site API from Optimizely — 2 operation(s) for site.
  name: Optimizely Site API
  slug: optimizely-site-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Specifications API from Optimizely — 7 operation(s) for specifications.
  name: Optimizely Specifications API
  slug: optimizely-specifications-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Spire Logs API from Optimizely — 2 operation(s) for spire logs.
  name: Optimizely Spire Logs API
  slug: optimizely-spire-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Spreedly API from Optimizely — 2 operation(s) for spreedly.
  name: Optimizely Spreedly API
  slug: optimizely-spreedly-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Spreedly Config API from Optimizely — 1 operation(s) for spreedly config.
  name: Optimizely Spreedly Config API
  slug: optimizely-spreedly-config-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Sso Clients API from Optimizely — 2 operation(s) for sso clients.
  name: Optimizely Sso Clients API
  slug: optimizely-sso-clients-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The State Tax Exemptions API from Optimizely — 5 operation(s) for state tax exemptions.
  name: Optimizely State Tax Exemptions API
  slug: optimizely-state-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The States API from Optimizely — 9 operation(s) for states.
  name: Optimizely States API
  slug: optimizely-states-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Structured Contents API from Optimizely — 11 operation(s) for structured contents.
  name: Optimizely Structured Contents API
  slug: optimizely-structured-contents-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Style Classes API from Optimizely — 8 operation(s) for style classes.
  name: Optimizely Style Classes API
  slug: optimizely-style-classes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Style Trait Value Products API from Optimizely — 5 operation(s) for style trait value products.
  name: Optimizely Style Trait Value Products API
  slug: optimizely-style-trait-value-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Style Trait Values API from Optimizely — 6 operation(s) for style trait values.
  name: Optimizely Style Trait Values API
  slug: optimizely-style-trait-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Style Traits API from Optimizely — 6 operation(s) for style traits.
  name: Optimizely Style Traits API
  slug: optimizely-style-traits-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage information about Subject Access Requests (includes GDPR)
  name: Optimizely Subject Access Requests API
  slug: optimizely-subject-access-requests-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Subscription Lines API from Optimizely — 5 operation(s) for subscription lines.
  name: Optimizely Subscription Lines API
  slug: optimizely-subscription-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Subscription Products API from Optimizely — 5 operation(s) for subscription products.
  name: Optimizely Subscription Products API
  slug: optimizely-subscription-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Subscriptions API from Optimizely — 9 operation(s) for subscriptions.
  name: Optimizely Subscriptions API
  slug: optimizely-subscriptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System Files API from Optimizely — 2 operation(s) for system files.
  name: Optimizely System Files API
  slug: optimizely-system-files-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System Folders API from Optimizely — 1 operation(s) for system folders.
  name: Optimizely System Folders API
  slug: optimizely-system-folders-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System List Values API from Optimizely — 7 operation(s) for system list values.
  name: Optimizely System List Values API
  slug: optimizely-system-list-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System Lists API from Optimizely — 8 operation(s) for system lists.
  name: Optimizely System Lists API
  slug: optimizely-system-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System Settings API from Optimizely — 14 operation(s) for system settings.
  name: Optimizely System Settings API
  slug: optimizely-system-settings-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Task Step API from Optimizely — 1 operation(s) for task step.
  name: Optimizely Task Step API
  slug: optimizely-task-step-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Tax Exemptions API from Optimizely — 11 operation(s) for tax exemptions.
  name: Optimizely Tax Exemptions API
  slug: optimizely-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Team Management API from Optimizely — 2 operation(s) for team management.
  name: Optimizely Team Management API
  slug: optimizely-team-management-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Teams API from Optimizely — 2 operation(s) for teams.
  name: Optimizely Teams API
  slug: optimizely-teams-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Telemetry API from Optimizely — 2 operation(s) for telemetry.
  name: Optimizely Telemetry API
  slug: optimizely-telemetry-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Templates API from Optimizely — 2 operation(s) for templates.
  name: Optimizely Templates API
  slug: optimizely-templates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Themes API from Optimizely — 5 operation(s) for themes.
  name: Optimizely Themes API
  slug: optimizely-themes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Token Ex Config API from Optimizely — 1 operation(s) for token ex config.
  name: Optimizely Token Ex Config API
  slug: optimizely-token-ex-config-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Tokenexconfig API from Optimizely — 1 operation(s) for tokenexconfig.
  name: Optimizely Tokenexconfig API
  slug: optimizely-tokenexconfig-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Track API from Optimizely — 1 operation(s) for track.
  name: Optimizely Track API
  slug: optimizely-track-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage transactional mails that are triggered by a recipient action or event
  name: Optimizely Transactional mails API
  slug: optimizely-transactional-mails-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Translation Dictionaries API from Optimizely — 5 operation(s) for translation dictionaries.
  name: Optimizely Translation Dictionaries API
  slug: optimizely-translation-dictionaries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Translation Properties API from Optimizely — 7 operation(s) for translation properties.
  name: Optimizely Translation Properties API
  slug: optimizely-translation-properties-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Translationdictionaries API from Optimizely — 1 operation(s) for translationdictionaries.
  name: Optimizely Translationdictionaries API
  slug: optimizely-translationdictionaries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Uploader API from Optimizely — 4 operation(s) for uploader.
  name: Optimizely Uploader API
  slug: optimizely-uploader-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: User related information for the current account
  name: Optimizely User API
  slug: optimizely-user-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Files API from Optimizely — 1 operation(s) for user files.
  name: Optimizely User Files API
  slug: optimizely-user-files-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Payment Profiles API from Optimizely — 5 operation(s) for user payment profiles.
  name: Optimizely User Payment Profiles API
  slug: optimizely-user-payment-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Email Lists API from Optimizely — 5 operation(s) for user profile email lists.
  name: Optimizely User Profile Email Lists API
  slug: optimizely-user-profile-email-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Passwords API from Optimizely — 5 operation(s) for user profile passwords.
  name: Optimizely User Profile Passwords API
  slug: optimizely-user-profile-passwords-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Websites API from Optimizely — 5 operation(s) for user profile websites.
  name: Optimizely User Profile Websites API
  slug: optimizely-user-profile-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Wish List Favorites API from Optimizely — 5 operation(s) for user profile wish list favorites.
  name: Optimizely User Profile Wish List Favorites API
  slug: optimizely-user-profile-wish-list-favorites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Wish List Hides API from Optimizely — 5 operation(s) for user profile wish list hides.
  name: Optimizely User Profile Wish List Hides API
  slug: optimizely-user-profile-wish-list-hides-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Wish List Tags API from Optimizely — 5 operation(s) for user profile wish list tags.
  name: Optimizely User Profile Wish List Tags API
  slug: optimizely-user-profile-wish-list-tags-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profiles API from Optimizely — 26 operation(s) for user profiles.
  name: Optimizely User Profiles API
  slug: optimizely-user-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: User Management
  name: Optimizely Users API
  slug: optimizely-users-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Variable Definitions
  name: Optimizely Variable Definitions API
  slug: optimizely-variable-definitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Variations
  name: Optimizely Variations API
  slug: optimizely-variations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vat Codes API from Optimizely — 6 operation(s) for vat codes.
  name: Optimizely Vat Codes API
  slug: optimizely-vat-codes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vendors API from Optimizely — 6 operation(s) for vendors.
  name: Optimizely Vendors API
  slug: optimizely-vendors-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Version Histories API from Optimizely — 6 operation(s) for version histories.
  name: Optimizely Version Histories API
  slug: optimizely-version-histories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Version History Actions API from Optimizely — 5 operation(s) for version history actions.
  name: Optimizely Version History Actions API
  slug: optimizely-version-history-actions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vmi Bins API from Optimizely — 9 operation(s) for vmi bins.
  name: Optimizely Vmi Bins API
  slug: optimizely-vmi-bins-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vmi Counts API from Optimizely — 5 operation(s) for vmi counts.
  name: Optimizely Vmi Counts API
  slug: optimizely-vmi-counts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vmi Locations API from Optimizely — 8 operation(s) for vmi locations.
  name: Optimizely Vmi Locations API
  slug: optimizely-vmi-locations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vmi Notes API from Optimizely — 5 operation(s) for vmi notes.
  name: Optimizely Vmi Notes API
  slug: optimizely-vmi-notes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The VmiBins API from Optimizely — 1 operation(s) for vmibins.
  name: Optimizely Vmi Bins API
  slug: optimizely-vmibins-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The VmiLocations API from Optimizely — 13 operation(s) for vmilocations.
  name: Optimizely Vmi Locations API
  slug: optimizely-vmilocations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Warehouse Alternates API from Optimizely — 5 operation(s) for warehouse alternates.
  name: Optimizely Warehouse Alternates API
  slug: optimizely-warehouse-alternates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Warehouse Websites API from Optimizely — 5 operation(s) for warehouse websites.
  name: Optimizely Warehouse Websites API
  slug: optimizely-warehouse-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Warehouses API from Optimizely — 13 operation(s) for warehouses.
  name: Optimizely Warehouses API
  slug: optimizely-warehouses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage webhooks
  name: Optimizely Webhooks API
  slug: optimizely-webhooks-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Allowed Customers API from Optimizely — 5 operation(s) for website allowed customers.
  name: Optimizely Website Allowed Customers API
  slug: optimizely-website-allowed-customers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Carriers API from Optimizely — 5 operation(s) for website carriers.
  name: Optimizely Website Carriers API
  slug: optimizely-website-carriers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Countries API from Optimizely — 5 operation(s) for website countries.
  name: Optimizely Website Countries API
  slug: optimizely-website-countries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Currencies API from Optimizely — 5 operation(s) for website currencies.
  name: Optimizely Website Currencies API
  slug: optimizely-website-currencies-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Dealers API from Optimizely — 5 operation(s) for website dealers.
  name: Optimizely Website Dealers API
  slug: optimizely-website-dealers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Languages API from Optimizely — 5 operation(s) for website languages.
  name: Optimizely Website Languages API
  slug: optimizely-website-languages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Product Cross Sells API from Optimizely — 5 operation(s) for website product cross sells.
  name: Optimizely Website Product Cross Sells API
  slug: optimizely-website-product-cross-sells-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Promotions API from Optimizely — 5 operation(s) for website promotions.
  name: Optimizely Website Promotions API
  slug: optimizely-website-promotions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Sitemaps API from Optimizely — 5 operation(s) for website sitemaps.
  name: Optimizely Website Sitemaps API
  slug: optimizely-website-sitemaps-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website States API from Optimizely — 5 operation(s) for website states.
  name: Optimizely Website States API
  slug: optimizely-website-states-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Websites API from Optimizely — 41 operation(s) for websites.
  name: Optimizely Websites API
  slug: optimizely-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Customer Additions API from Optimizely — 5 operation(s) for wish list customer additions.
  name: Optimizely Wish List Customer Additions API
  slug: optimizely-wish-list-customer-additions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Customer Exceptions API from Optimizely — 5 operation(s) for wish list customer exceptions.
  name: Optimizely Wish List Customer Exceptions API
  slug: optimizely-wish-list-customer-exceptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Customers API from Optimizely — 5 operation(s) for wish list customers.
  name: Optimizely Wish List Customers API
  slug: optimizely-wish-list-customers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Email Schedules API from Optimizely — 5 operation(s) for wish list email schedules.
  name: Optimizely Wish List Email Schedules API
  slug: optimizely-wish-list-email-schedules-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Products API from Optimizely — 5 operation(s) for wish list products.
  name: Optimizely Wish List Products API
  slug: optimizely-wish-list-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Shares API from Optimizely — 5 operation(s) for wish list shares.
  name: Optimizely Wish List Shares API
  slug: optimizely-wish-list-shares-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish Lists API from Optimizely — 18 operation(s) for wish lists.
  name: Optimizely Wish Lists API
  slug: optimizely-wish-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wishlists API from Optimizely — 12 operation(s) for wishlists.
  name: Optimizely Wishlists API
  slug: optimizely-wishlists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Work Requests API from Optimizely — 13 operation(s) for work requests.
  name: Optimizely Work Requests API
  slug: optimizely-work-requests-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Workflows API from Optimizely — 2 operation(s) for workflows.
  name: Optimizely Workflows API
  slug: optimizely-workflows-api
artifact_total: 608
asyncapis:
- description: The Optimizely Content Marketing Platform (CMP) provides webhook notifications when content events occur, such as when assets are published, tasks are completed or modified, and content items are upda
  name: Optimizely CMP Webhooks
  slug: optimizely-cmp-asyncapi
- description: Optimizely Feature Experimentation provides webhook notifications when configuration changes occur, such as datafile updates. Webhooks notify external servers of changes, eliminating the need to const
  name: Optimizely Feature Experimentation Webhooks
  slug: optimizely-feature-experimentation-asyncapi
- description: ''
  name: Optimizely Webhooks
  slug: optimizely-webhooks
collections:
- collection_type: postman
  name: Optimizely Campaign REST Assets API
  slug: postman-optimizely-assets-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Attributes API
  slug: postman-optimizely-attributes-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Audiences API
  slug: postman-optimizely-audiences-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Campaigns API
  slug: postman-optimizely-campaigns-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalog Entries API
  slug: postman-optimizely-catalog-entries-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalog Entry Relations API
  slug: postman-optimizely-catalog-entry-relations-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalog Nodes API
  slug: postman-optimizely-catalog-nodes-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalogs API
  slug: postman-optimizely-catalogs-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Content API
  slug: postman-optimizely-content-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Content Types API
  slug: postman-optimizely-content-types-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Customers API
  slug: postman-optimizely-customers-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Environments API
  slug: postman-optimizely-environments-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Events API
  slug: postman-optimizely-events-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Experiments API
  slug: postman-optimizely-experiments-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Extensions API
  slug: postman-optimizely-extensions-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Features API
  slug: postman-optimizely-features-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Flags API
  slug: postman-optimizely-flags-api
- collection_type: postman
  name: Optimizely Campaign REST Assets GraphQL API
  slug: postman-optimizely-graphql-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Labels API
  slug: postman-optimizely-labels-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Mailing Lists API
  slug: postman-optimizely-mailing-lists-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Objects API
  slug: postman-optimizely-objects-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Orders API
  slug: postman-optimizely-orders-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Pages API
  slug: postman-optimizely-pages-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Profiles API
  slug: postman-optimizely-profiles-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Projects API
  slug: postman-optimizely-projects-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Recipients API
  slug: postman-optimizely-recipients-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Rulesets API
  slug: postman-optimizely-rulesets-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Schema API
  slug: postman-optimizely-schema-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Segments API
  slug: postman-optimizely-segments-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Sites API
  slug: postman-optimizely-sites-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Smart Campaigns API
  slug: postman-optimizely-smart-campaigns-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Tasks API
  slug: postman-optimizely-tasks-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Transactional Mail API
  slug: postman-optimizely-transactional-mail-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Unsubscribes API
  slug: postman-optimizely-unsubscribes-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Optimizely Campaign REST Assets API
  slug: open-optimizely-assets-api
- collection_type: open
  name: Optimizely Campaign REST Assets Attributes API
  slug: open-optimizely-attributes-api
- collection_type: open
  name: Optimizely Campaign REST Assets Audiences API
  slug: open-optimizely-audiences-api
- collection_type: open
  name: Optimizely Campaign REST API
  slug: open-optimizely-campaign
- collection_type: open
  name: Optimizely Campaign REST Assets Campaigns API
  slug: open-optimizely-campaigns-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalog Entries API
  slug: open-optimizely-catalog-entries-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalog Entry Relations API
  slug: open-optimizely-catalog-entry-relations-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalog Nodes API
  slug: open-optimizely-catalog-nodes-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalogs API
  slug: open-optimizely-catalogs-api
- collection_type: open
  name: Optimizely CMP Open REST API
  slug: open-optimizely-cmp
- collection_type: open
  name: Optimizely Commerce Service API
  slug: open-optimizely-commerce-service
- collection_type: open
  name: Optimizely Campaign REST Assets Content API
  slug: open-optimizely-content-api
- collection_type: open
  name: Optimizely Content Delivery API
  slug: open-optimizely-content-delivery
- collection_type: open
  name: Optimizely Content Management API
  slug: open-optimizely-content-management
- collection_type: open
  name: Optimizely Campaign REST Assets Content Types API
  slug: open-optimizely-content-types-api
- collection_type: open
  name: Optimizely Campaign REST Assets Customers API
  slug: open-optimizely-customers-api
- collection_type: open
  name: Optimizely Data Platform REST API
  slug: open-optimizely-data-platform
- collection_type: open
  name: Optimizely Campaign REST Assets Environments API
  slug: open-optimizely-environments-api
- collection_type: open
  name: Optimizely Campaign REST Assets Events API
  slug: open-optimizely-events-api
- collection_type: open
  name: Optimizely Campaign REST Assets Experiments API
  slug: open-optimizely-experiments-api
- collection_type: open
  name: Optimizely Campaign REST Assets Extensions API
  slug: open-optimizely-extensions-api
- collection_type: open
  name: Optimizely Feature Experimentation REST API
  slug: open-optimizely-feature-experimentation
- collection_type: open
  name: Optimizely Campaign REST Assets Features API
  slug: open-optimizely-features-api
- collection_type: open
  name: Optimizely Campaign REST Assets Flags API
  slug: open-optimizely-flags-api
- collection_type: open
  name: Optimizely Graph API
  slug: open-optimizely-graph
- collection_type: open
  name: Optimizely Campaign REST Assets GraphQL API
  slug: open-optimizely-graphql-api
- collection_type: open
  name: Optimizely Campaign REST Assets Labels API
  slug: open-optimizely-labels-api
- collection_type: open
  name: Optimizely Campaign REST Assets Mailing Lists API
  slug: open-optimizely-mailing-lists-api
- collection_type: open
  name: Optimizely Campaign REST Assets Objects API
  slug: open-optimizely-objects-api
- collection_type: open
  name: Optimizely Campaign REST Assets Orders API
  slug: open-optimizely-orders-api
- collection_type: open
  name: Optimizely Campaign REST Assets Pages API
  slug: open-optimizely-pages-api
- collection_type: open
  name: Optimizely Campaign REST Assets Profiles API
  slug: open-optimizely-profiles-api
- collection_type: open
  name: Optimizely Campaign REST Assets Projects API
  slug: open-optimizely-projects-api
- collection_type: open
  name: Optimizely Campaign REST Assets Recipients API
  slug: open-optimizely-recipients-api
- collection_type: open
  name: Optimizely Campaign REST Assets Rulesets API
  slug: open-optimizely-rulesets-api
- collection_type: open
  name: Optimizely Campaign REST Assets Schema API
  slug: open-optimizely-schema-api
- collection_type: open
  name: Optimizely Campaign REST Assets Segments API
  slug: open-optimizely-segments-api
- collection_type: open
  name: Optimizely Campaign REST Assets Sites API
  slug: open-optimizely-sites-api
- collection_type: open
  name: Optimizely Campaign REST Assets Smart Campaigns API
  slug: open-optimizely-smart-campaigns-api
- collection_type: open
  name: Optimizely Campaign REST Assets Tasks API
  slug: open-optimizely-tasks-api
- collection_type: open
  name: Optimizely Campaign REST Assets Transactional Mail API
  slug: open-optimizely-transactional-mail-api
- collection_type: open
  name: Optimizely Campaign REST Assets Unsubscribes API
  slug: open-optimizely-unsubscribes-api
- collection_type: open
  name: Optimizely Web Experimentation REST API
  slug: open-optimizely-web-experimentation
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/optimizely-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-feature-experimentation-flags-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-flags-scheduling-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-permission-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-agent-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-event-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-edge-decider-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-odp-advanced-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-graph-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-cmp-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-campaign-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-configured-commerce-admin-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-cms-content-delivery-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-content-recommendations-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/optimizely-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.developers.optimizely.com/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/optimizely-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/optimizely-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optimizely-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/optimizely-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/optimizely-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/optimizely-cli.yml
- group: design
  title: ''
  type: Components
  url: components/optimizely-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/optimizely-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/optimizely-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/optimizely-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/optimizely-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/optimizely-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.optimizely.com/trust-center/compliance
- group: auth
  title: ''
  type: Security
  url: https://www.optimizely.com/trust-center/security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optimizely-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.optimizely.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/optimizely-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/optimizely-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/optimizely-feature-experimentation-asyncapi.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/optimizely-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/optimizely-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-experimentation-v2-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developers.optimizely.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developers.optimizely.com/web-experimentation/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developers.optimizely.com/feature-experimentation/docs/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.optimizely.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.optimizely.com/free-trial/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.optimizely.com/hc/en-us/
- group: operate
  title: ''
  type: Community
  url: https://world.optimizely.com/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/optimizely-vocabulary.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/optimizely/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optimizely-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/optimizely-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optimizely-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optimizely-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optimizely-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/optimizely-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/optimizely
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/optimizely
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.developers.optimizely.com/
- group: company
  title: ''
  type: Website
  url: https://www.optimizely.com/
- group: company
  title: ''
  type: Blog
  url: https://www.optimizely.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.optimizely.com/
- group: start
  title: ''
  type: Login
  url: https://app.optimizely.com/signin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optimizely.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optimizely.com/legal/terms/
created: '2025-03-04'
description: Optimizely is a digital experience platform that provides A/B testing, feature flagging, content management, and commerce solutions for enterprises. Their developer platform offers a comprehensive suite of REST and GraphQL APIs spanning experimentation, content delivery, customer data, campaign management, and e-commerce capabilities.
features:
- 'Entry: ~$36K/year for basic Optimizely use'
- 'Mid: ~$63,700 per 10M impressions for Web Experimentation'
- 'Enterprise: $200K-$400K+/year for full DXP suite'
- 'Modular: pick CMS / Commerce / Experimentation independently'
- Web Experimentation (A/B + multivariate)
- Feature Experimentation (server-side flags)
- Personalization with audiences and Stats Engine
- Content Cloud (CMS)
- Commerce Cloud and Configured Commerce
- Optimizely AI Copilot
- REST API at api.optimizely.com
- Default 100 req/min/project
- OAuth 2.0 + Personal API tokens
- Webhooks for project events
- Datafile-based Feature Experimentation SDKs (10+)
- Stats Engine with Sequential Testing
finops:
- name: Optimizely Finops
  service_category: Digital Experience Platform
  slug: optimizely-finops
graphqls:
- description: Optimizely Graph is a unified content query and delivery service that provides access to content across Optimizely products through a single GraphQL API. It enables flexible data retrieval, high-perfo
  name: Optimizely GraphQL API
  slug: optimizely-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optimizely.png
json_schemas:
- name: Asset
  property_count: 6
  slug: optimizely-asset
- name: AssetInput
  property_count: 3
  slug: optimizely-assetinput
- name: Attribute
  property_count: 6
  slug: optimizely-attribute
- name: Audience
  property_count: 7
  slug: optimizely-audience
- name: AudienceInput
  property_count: 4
  slug: optimizely-audienceinput
- name: Campaign
  property_count: 8
  slug: optimizely-campaign
- name: CampaignInput
  property_count: 3
  slug: optimizely-campaigninput
- name: Catalog
  property_count: 6
  slug: optimizely-catalog
- name: CatalogEntry
  property_count: 8
  slug: optimizely-catalogentry
- name: CatalogEntryInput
  property_count: 5
  slug: optimizely-catalogentryinput
- name: CatalogInput
  property_count: 4
  slug: optimizely-cataloginput
- name: CatalogNode
  property_count: 8
  slug: optimizely-catalognode
- name: CatalogNodeInput
  property_count: 5
  slug: optimizely-catalognodeinput
- name: CmpCampaign
  property_count: 9
  slug: optimizely-cmpcampaign
- name: CmpContent
  property_count: 9
  slug: optimizely-cmpcontent
- name: ContentInput
  property_count: 7
  slug: optimizely-contentinput
- name: ContentItem
  property_count: 13
  slug: optimizely-contentitem
- name: ContentPatch
  property_count: 3
  slug: optimizely-contentpatch
- name: ContentType
  property_count: 5
  slug: optimizely-contenttype
- name: Optimizely Customer Profile
  property_count: 5
  slug: optimizely-customer-profile
- name: Customer
  property_count: 5
  slug: optimizely-customer
- name: Environment
  property_count: 8
  slug: optimizely-environment
- name: EnvironmentInput
  property_count: 3
  slug: optimizely-environmentinput
- name: Event
  property_count: 7
  slug: optimizely-event
- name: EventInput
  property_count: 4
  slug: optimizely-eventinput
- name: Optimizely Experiment
  property_count: 13
  slug: optimizely-experiment
- name: ExperimentInput
  property_count: 4
  slug: optimizely-experimentinput
- name: ExperimentResults
  property_count: 5
  slug: optimizely-experimentresults
- name: Extension
  property_count: 6
  slug: optimizely-extension
- name: Optimizely Feature Flag
  property_count: 9
  slug: optimizely-feature-flag
- name: Feature
  property_count: 6
  slug: optimizely-feature
- name: Flag
  property_count: 9
  slug: optimizely-flag
- name: FlagEnvironment
  property_count: 2
  slug: optimizely-flagenvironment
- name: FlagInput
  property_count: 5
  slug: optimizely-flaginput
- name: FlagVariation
  property_count: 3
  slug: optimizely-flagvariation
- name: FlagVariationInput
  property_count: 3
  slug: optimizely-flagvariationinput
- name: GraphQLRequest
  property_count: 3
  slug: optimizely-graphqlrequest
- name: GraphQLResponse
  property_count: 3
  slug: optimizely-graphqlresponse
- name: Label
  property_count: 3
  slug: optimizely-label
- name: MailingList
  property_count: 4
  slug: optimizely-mailinglist
- name: Metric
  property_count: 5
  slug: optimizely-metric
- name: NodeRelation
  property_count: 3
  slug: optimizely-noderelation
- name: NodeRelationInput
  property_count: 2
  slug: optimizely-noderelationinput
- name: ObjectInput
  property_count: 2
  slug: optimizely-objectinput
- name: OdpObject
  property_count: 5
  slug: optimizely-odpobject
- name: Order
  property_count: 9
  slug: optimizely-order
- name: Page
  property_count: 8
  slug: optimizely-page
- name: PageInput
  property_count: 5
  slug: optimizely-pageinput
- name: Pagination
  property_count: 3
  slug: optimizely-pagination
- name: Profile
  property_count: 11
  slug: optimizely-profile
- name: ProfileInput
  property_count: 2
  slug: optimizely-profileinput
- name: Project
  property_count: 8
  slug: optimizely-project
- name: ProjectInput
  property_count: 2
  slug: optimizely-projectinput
- name: Recipient
  property_count: 8
  slug: optimizely-recipient
- name: RecipientInput
  property_count: 4
  slug: optimizely-recipientinput
- name: Rule
  property_count: 6
  slug: optimizely-rule
- name: RuleInput
  property_count: 5
  slug: optimizely-ruleinput
- name: Ruleset
  property_count: 1
  slug: optimizely-ruleset
- name: RulesetInput
  property_count: 1
  slug: optimizely-rulesetinput
- name: SchemaField
  property_count: 4
  slug: optimizely-schemafield
- name: SchemaFieldInput
  property_count: 4
  slug: optimizely-schemafieldinput
- name: SchemaObject
  property_count: 4
  slug: optimizely-schemaobject
- name: SchemaObjectInput
  property_count: 2
  slug: optimizely-schemaobjectinput
- name: Segment
  property_count: 3
  slug: optimizely-segment
- name: Site
  property_count: 4
  slug: optimizely-site
- name: SmartCampaign
  property_count: 5
  slug: optimizely-smartcampaign
- name: Task
  property_count: 11
  slug: optimizely-task
- name: TaskInput
  property_count: 6
  slug: optimizely-taskinput
- name: TransactionalMailInput
  property_count: 3
  slug: optimizely-transactionalmailinput
- name: TransactionalMailResponse
  property_count: 2
  slug: optimizely-transactionalmailresponse
- name: Unsubscribe
  property_count: 3
  slug: optimizely-unsubscribe
- name: UnsubscribeInput
  property_count: 1
  slug: optimizely-unsubscribeinput
- name: Variable
  property_count: 3
  slug: optimizely-variable
- name: VariableInput
  property_count: 3
  slug: optimizely-variableinput
- name: Variation
  property_count: 4
  slug: optimizely-variation
- name: VariationInput
  property_count: 2
  slug: optimizely-variationinput
json_structures:
- name: Optimizely Structure
  property_count: 0
  slug: optimizely-structure
jsonld:
- class_count: 0
  name: Optimizely Context
  property_count: 12
  slug: optimizely-context
layout: provider
mcp_servers:
- description: ''
  name: Optimizely MCP Server
  slug: optimizely-mcp-server
modified: '2026-08-13'
name: Optimizely
nav: Providers
network: true
overview: 'Optimizely publishes 419 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Attributes API, Audiences API, and 416 more. Tagged areas include A/B Testing, Content Management, Customer Data, E-Commerce, and Experimentation.


  The Optimizely catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Optimizely''s developer surface includes CLI, sandbox, changelog, documentation, API reference, getting-started guide, pricing, and 56 more developer resources.'
plans:
- name: Optimizely Plans Pricing
  plan_count: 3
  slug: optimizely-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 8
  name: Optimizely Rate Limits
  slug: optimizely-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Optimizely API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: optimizely-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Optimizely API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: optimizely-jsonschema-spectral-rules
scopes:
- name: Optimizely Scopes
  scope_count: 6
  slug: optimizely-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: exemplar
  composite: 71.6
  coverage:
    artifact_dirs: 36
    catalog_gap: 42.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 47.0
    contract_quality: 66.9
    developer_ergonomics: 71.4
    discoverability: 87.0
    governance: 47.0
    operational_transparency: 84.2
  previous_composite: 71.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 95.5
      derived: 0
      marker_coverage: 0.0
      total: 419
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/screenshots/optimizely-2026-08-07T190808.png
security:
- kind: authentication
  name: Optimizely Authentication
  slug: optimizely-authentication
  summary_line: oauth2/http/apiKey · 10 schemes
- kind: domain-security
  name: Optimizely Domain Security
  slug: optimizely-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Optimizely Vulnerability Disclosure
  slug: optimizely-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Optimizely Trust Center
  slug: optimizely-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA
slug: optimizely
tags:
- A/B Testing
- Content Management
- Customer Data
- E-Commerce
- Experimentation
- Feature Flags
- Marketing
website: https://www.optimizely.com/
---
