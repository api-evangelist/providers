---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1218
  human_in_the_loop: 20
  name: Automattic Agentic Access
  operation_count: 2384
  slug: automattic-agentic-access
  summary_line: 2384 operations · 1218 acting · 20 human-in-the-loop
api_count: 2
apis:
- description: Automattic's hosted Model Context Protocol server for WordPress.com. Streamable HTTP transport secured with OAuth 2.1 (PKCE S256, dynamic client registration, token rotation, no client secret). Twelve
  name: WordPress.com MCP Server
  slug: wordpresscom-mcp-server
- description: The GraphQL API for WordPress VIP, Automattic's enterprise WordPress and Node.js platform. Documented operation categories cover apps, domains, organizations, users, integrations, security and observa
  name: WordPress VIP Platform API
  slug: wordpress-vip-platform-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The a8c-lore API from Automattic — 2 operation(s) for a8c-lore.
  name: Automattic A8c Lore API
  slug: automattic-a8c-lore-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The a8cmentorship API from Automattic — 1 operation(s) for a8cmentorship.
  name: Automattic A8cmentorship API
  slug: automattic-a8cmentorship-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The abilities API from Automattic — 1 operation(s) for abilities.
  name: Automattic Abilities API
  slug: automattic-abilities-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The activity API from Automattic — 8 operation(s) for activity.
  name: Automattic Activity API
  slug: automattic-activity-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The activity-log-events API from Automattic — 4 operation(s) for activity-log-events.
  name: Automattic Activity Log Events API
  slug: automattic-activity-log-events-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The activitypub API from Automattic — 1 operation(s) for activitypub.
  name: Automattic Activitypub API
  slug: automattic-activitypub-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The adflow API from Automattic — 1 operation(s) for adflow.
  name: Automattic Adflow API
  slug: automattic-adflow-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The admin-bar API from Automattic — 1 operation(s) for admin-bar.
  name: Automattic Admin Bar API
  slug: automattic-admin-bar-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The admin-color API from Automattic — 1 operation(s) for admin-color.
  name: Automattic Admin Color API
  slug: automattic-admin-color-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The admin-menu API from Automattic — 1 operation(s) for admin-menu.
  name: Automattic Admin Menu API
  slug: automattic-admin-menu-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The agency API from Automattic — 88 operation(s) for agency.
  name: Automattic Agency API
  slug: automattic-agency-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The agency-client API from Automattic — 8 operation(s) for agency-client.
  name: Automattic Agency Client API
  slug: automattic-agency-client-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The agents-manager API from Automattic — 1 operation(s) for agents-manager.
  name: Automattic Agents Manager API
  slug: automattic-agents-manager-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The ai-agents-settings API from Automattic — 1 operation(s) for ai-agents-settings.
  name: Automattic AI Agents Settings API
  slug: automattic-ai-agents-settings-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The ai API from Automattic — 17 operation(s) for ai.
  name: Automattic AI API
  slug: automattic-ai-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The ai-image API from Automattic — 1 operation(s) for ai-image.
  name: Automattic AI Image API
  slug: automattic-ai-image-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The ai-launchpad API from Automattic — 6 operation(s) for ai-launchpad.
  name: Automattic AI Launchpad API
  slug: automattic-ai-launchpad-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The akismet API from Automattic — 1 operation(s) for akismet.
  name: Automattic Akismet API
  slug: automattic-akismet-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The alerts API from Automattic — 3 operation(s) for alerts.
  name: Automattic Alerts API
  slug: automattic-alerts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The alternates API from Automattic — 1 operation(s) for alternates.
  name: Automattic Alternates API
  slug: automattic-alternates-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The analytics API from Automattic — 25 operation(s) for analytics.
  name: Automattic Analytics API
  slug: automattic-analytics-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The analyze-url API from Automattic — 1 operation(s) for analyze-url.
  name: Automattic Analyze URL API
  slug: automattic-analyze-url-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The app-media API from Automattic — 1 operation(s) for app-media.
  name: Automattic App Media API
  slug: automattic-app-media-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The articles API from Automattic — 1 operation(s) for articles.
  name: Automattic Articles API
  slug: automattic-articles-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The atomic API from Automattic — 2 operation(s) for atomic.
  name: Automattic Atomic API
  slug: automattic-atomic-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The atomic-migration-status API from Automattic — 3 operation(s) for atomic-migration-status.
  name: Automattic Atomic Migration Status API
  slug: automattic-atomic-migration-status-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The auth API from Automattic — 8 operation(s) for auth.
  name: Automattic Auth API
  slug: automattic-auth-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The automated-migration API from Automattic — 6 operation(s) for automated-migration.
  name: Automattic Automated Migration API
  slug: automattic-automated-migration-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The backup API from Automattic — 1 operation(s) for backup.
  name: Automattic Backup API
  slug: automattic-backup-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The batch API from Automattic — 1 operation(s) for batch.
  name: Automattic Batch API
  slug: automattic-batch-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The big-sky API from Automattic — 11 operation(s) for big-sky.
  name: Automattic Big Sky API
  slug: automattic-big-sky-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The blaze API from Automattic — 5 operation(s) for blaze.
  name: Automattic Blaze API
  slug: automattic-blaze-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The block-directory API from Automattic — 1 operation(s) for block-directory.
  name: Automattic Block Directory API
  slug: automattic-block-directory-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The block-editor API from Automattic — 6 operation(s) for block-editor.
  name: Automattic Block Editor API
  slug: automattic-block-editor-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The block-layouts API from Automattic — 1 operation(s) for block-layouts.
  name: Automattic Block Layouts API
  slug: automattic-block-layouts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The block-patterns API from Automattic — 2 operation(s) for block-patterns.
  name: Automattic Block Patterns API
  slug: automattic-block-patterns-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The block-previews API from Automattic — 2 operation(s) for block-previews.
  name: Automattic Block Previews API
  slug: automattic-block-previews-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The block-recipes API from Automattic — 2 operation(s) for block-recipes.
  name: Automattic Block Recipes API
  slug: automattic-block-recipes-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The block-renderer API from Automattic — 4 operation(s) for block-renderer.
  name: Automattic Block Renderer API
  slug: automattic-block-renderer-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The block-types API from Automattic — 3 operation(s) for block-types.
  name: Automattic Block Types API
  slug: automattic-block-types-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The blocks API from Automattic — 6 operation(s) for blocks.
  name: Automattic Blocks API
  slug: automattic-blocks-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The blog-stats API from Automattic — 1 operation(s) for blog-stats.
  name: Automattic Blog Stats API
  slug: automattic-blog-stats-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The blogging-prompts API from Automattic — 2 operation(s) for blogging-prompts.
  name: Automattic Blogging Prompts API
  slug: automattic-blogging-prompts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The blueprint-archive API from Automattic — 1 operation(s) for blueprint-archive.
  name: Automattic Blueprint Archive API
  slug: automattic-blueprint-archive-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The blueprint-archive-import API from Automattic — 1 operation(s) for blueprint-archive-import.
  name: Automattic Blueprint Archive Import API
  slug: automattic-blueprint-archive-import-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The breakingbot API from Automattic — 2 operation(s) for breakingbot.
  name: Automattic Breakingbot API
  slug: automattic-breakingbot-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The business-hours API from Automattic — 1 operation(s) for business-hours.
  name: Automattic Business Hours API
  slug: automattic-business-hours-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The calypso-slack-channel-status API from Automattic — 1 operation(s) for calypso-slack-channel-status.
  name: Automattic Calypso Slack Channel Status API
  slug: automattic-calypso-slack-channel-status-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The categories API from Automattic — 2 operation(s) for categories.
  name: Automattic Categories API
  slug: automattic-categories-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The ceo-voice-agent API from Automattic — 3 operation(s) for ceo-voice-agent.
  name: Automattic Ceo Voice Agent API
  slug: automattic-ceo-voice-agent-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The checkGoogleDocVisibility API from Automattic — 1 operation(s) for checkgoogledocvisibility.
  name: Automattic Check Google Doc Visibility API
  slug: automattic-checkgoogledocvisibility-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The ciab API from Automattic — 1 operation(s) for ciab.
  name: Automattic Ciab API
  slug: automattic-ciab-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The cmp API from Automattic — 3 operation(s) for cmp.
  name: Automattic Cmp API
  slug: automattic-cmp-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The colors API from Automattic — 4 operation(s) for colors.
  name: Automattic Colors API
  slug: automattic-colors-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The coming-soon API from Automattic — 1 operation(s) for coming-soon.
  name: Automattic Coming Soon API
  slug: automattic-coming-soon-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The comments API from Automattic — 14 operation(s) for comments.
  name: Automattic Comments API
  slug: automattic-comments-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The comments-tree API from Automattic — 1 operation(s) for comments-tree.
  name: Automattic Comments Tree API
  slug: automattic-comments-tree-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The commercial-classification API from Automattic — 1 operation(s) for commercial-classification.
  name: Automattic Commercial Classification API
  slug: automattic-commercial-classification-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The common-block-layouts API from Automattic — 1 operation(s) for common-block-layouts.
  name: Automattic Common Block Layouts API
  slug: automattic-common-block-layouts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The common-starter-site-designs API from Automattic — 1 operation(s) for common-starter-site-designs.
  name: Automattic Common Starter Site Designs API
  slug: automattic-common-starter-site-designs-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The concierge API from Automattic — 11 operation(s) for concierge.
  name: Automattic Concierge API
  slug: automattic-concierge-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The content-research API from Automattic — 2 operation(s) for content-research.
  name: Automattic Content Research API
  slug: automattic-content-research-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The copy-from-site API from Automattic — 1 operation(s) for copy-from-site.
  name: Automattic Copy From Site API
  slug: automattic-copy-from-site-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The country-codes API from Automattic — 1 operation(s) for country-codes.
  name: Automattic Country Codes API
  slug: automattic-country-codes-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The courses API from Automattic — 2 operation(s) for courses.
  name: Automattic Courses API
  slug: automattic-courses-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The currency-overrides API from Automattic — 1 operation(s) for currency-overrides.
  name: Automattic Currency Overrides API
  slug: automattic-currency-overrides-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The dashboard API from Automattic — 5 operation(s) for dashboard.
  name: Automattic Dashboard API
  slug: automattic-dashboard-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The dashboards API from Automattic — 3 operation(s) for dashboards.
  name: Automattic Dashboards API
  slug: automattic-dashboards-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The deepl API from Automattic — 1 operation(s) for deepl.
  name: Automattic Deepl API
  slug: automattic-deepl-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The dictation-client-secret API from Automattic — 3 operation(s) for dictation-client-secret.
  name: Automattic Dictation Client Secret API
  slug: automattic-dictation-client-secret-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The discount API from Automattic — 1 operation(s) for discount.
  name: Automattic Discount API
  slug: automattic-discount-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The do-it-for-me API from Automattic — 1 operation(s) for do-it-for-me.
  name: Automattic Do It For Me API
  slug: automattic-do-it-for-me-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The domain-connect API from Automattic — 5 operation(s) for domain-connect.
  name: Automattic Domain Connect API
  slug: automattic-domain-connect-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The domains API from Automattic — 25 operation(s) for domains.
  name: Automattic Domains API
  slug: automattic-domains-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The editor API from Automattic — 1 operation(s) for editor.
  name: Automattic Editor API
  slug: automattic-editor-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The editor-assets API from Automattic — 1 operation(s) for editor-assets.
  name: Automattic Editor Assets API
  slug: automattic-editor-assets-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The email-like API from Automattic — 1 operation(s) for email-like.
  name: Automattic Email Like API
  slug: automattic-email-like-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The email-preview API from Automattic — 1 operation(s) for email-preview.
  name: Automattic Email Preview API
  slug: automattic-email-preview-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The emails API from Automattic — 10 operation(s) for emails.
  name: Automattic Emails API
  slug: automattic-emails-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The enterpret-webhook API from Automattic — 1 operation(s) for enterpret-webhook.
  name: Automattic Enterpret Webhook API
  slug: automattic-enterpret-webhook-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The experiments API from Automattic — 29 operation(s) for experiments.
  name: Automattic Experiments API
  slug: automattic-experiments-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The external-contributors API from Automattic — 3 operation(s) for external-contributors.
  name: Automattic External Contributors API
  slug: automattic-external-contributors-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The external-media API from Automattic — 7 operation(s) for external-media.
  name: Automattic External Media API
  slug: automattic-external-media-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The external-services API from Automattic — 1 operation(s) for external-services.
  name: Automattic External Services API
  slug: automattic-external-services-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The feedback API from Automattic — 14 operation(s) for feedback.
  name: Automattic Feedback API
  slug: automattic-feedback-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The follow API from Automattic — 4 operation(s) for follow.
  name: Automattic Follow API
  slug: automattic-follow-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The following API from Automattic — 2 operation(s) for following.
  name: Automattic Following API
  slug: automattic-following-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The font-collections API from Automattic — 2 operation(s) for font-collections.
  name: Automattic Font Collections API
  slug: automattic-font-collections-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The font-families API from Automattic — 4 operation(s) for font-families.
  name: Automattic Font Families API
  slug: automattic-font-families-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The freshly-pressed API from Automattic — 1 operation(s) for freshly-pressed.
  name: Automattic Freshly Pressed API
  slug: automattic-freshly-pressed-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The fsor-airtable-report API from Automattic — 1 operation(s) for fsor-airtable-report.
  name: Automattic Fsor Airtable Report API
  slug: automattic-fsor-airtable-report-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The general API from Automattic — 5 operation(s) for general.
  name: Automattic General API
  slug: automattic-general-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The github API from Automattic — 2 operation(s) for github.
  name: Automattic Github API
  slug: automattic-github-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The global-styles API from Automattic — 6 operation(s) for global-styles.
  name: Automattic Global Styles API
  slug: automattic-global-styles-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The global-styles-variation API from Automattic — 5 operation(s) for global-styles-variation.
  name: Automattic Global Styles Variation API
  slug: automattic-global-styles-variation-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The glossary API from Automattic — 2 operation(s) for glossary.
  name: Automattic Glossary API
  slug: automattic-glossary-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The goodreads API from Automattic — 1 operation(s) for goodreads.
  name: Automattic Goodreads API
  slug: automattic-goodreads-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The google-drive API from Automattic — 2 operation(s) for google-drive.
  name: Automattic Google Drive API
  slug: automattic-google-drive-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The grafana API from Automattic — 1 operation(s) for grafana.
  name: Automattic Grafana API
  slug: automattic-grafana-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The gravatar API from Automattic — 13 operation(s) for gravatar.
  name: Automattic Gravatar API
  slug: automattic-gravatar-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The gravatar-upload API from Automattic — 1 operation(s) for gravatar-upload.
  name: Automattic Gravatar Upload API
  slug: automattic-gravatar-upload-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The guidelines API from Automattic — 6 operation(s) for guidelines.
  name: Automattic Guidelines API
  slug: automattic-guidelines-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The gutenberg API from Automattic — 3 operation(s) for gutenberg.
  name: Automattic Gutenberg API
  slug: automattic-gutenberg-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The gutenpen API from Automattic — 3 operation(s) for gutenpen.
  name: Automattic Gutenpen API
  slug: automattic-gutenpen-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The hello API from Automattic — 1 operation(s) for hello.
  name: Automattic Hello API
  slug: automattic-hello-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The help API from Automattic — 22 operation(s) for help.
  name: Automattic Help API
  slug: automattic-help-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The home API from Automattic — 2 operation(s) for home.
  name: Automattic Home API
  slug: automattic-home-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The host-partners API from Automattic — 39 operation(s) for host-partners.
  name: Automattic Host Partners API
  slug: automattic-host-partners-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The hosting API from Automattic — 23 operation(s) for hosting.
  name: Automattic Hosting API
  slug: automattic-hosting-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The hosting-provider API from Automattic — 1 operation(s) for hosting-provider.
  name: Automattic Hosting Provider API
  slug: automattic-hosting-provider-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The iap API from Automattic — 3 operation(s) for iap.
  name: Automattic Iap API
  slug: automattic-iap-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The icon-collections API from Automattic — 2 operation(s) for icon-collections.
  name: Automattic Icon Collections API
  slug: automattic-icon-collections-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The icons API from Automattic — 3 operation(s) for icons.
  name: Automattic Icons API
  slug: automattic-icons-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The import API from Automattic — 4 operation(s) for import.
  name: Automattic Import API
  slug: automattic-import-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The imports API from Automattic — 2 operation(s) for imports.
  name: Automattic Imports API
  slug: automattic-imports-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The individual-subscriber-stats API from Automattic — 1 operation(s) for individual-subscriber-stats.
  name: Automattic Individual Subscriber Stats API
  slug: automattic-individual-subscriber-stats-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The insights API from Automattic — 2 operation(s) for insights.
  name: Automattic Insights API
  slug: automattic-insights-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The instagram API from Automattic — 3 operation(s) for instagram.
  name: Automattic Instagram API
  slug: automattic-instagram-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The instagram-gallery API from Automattic — 3 operation(s) for instagram-gallery.
  name: Automattic Instagram Gallery API
  slug: automattic-instagram-gallery-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The introductory-offers API from Automattic — 1 operation(s) for introductory-offers.
  name: Automattic Introductory Offers API
  slug: automattic-introductory-offers-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The invites API from Automattic — 7 operation(s) for invites.
  name: Automattic Invites API
  slug: automattic-invites-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The ip-to-geo API from Automattic — 1 operation(s) for ip-to-geo.
  name: Automattic Ip To Geo API
  slug: automattic-ip-to-geo-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-about API from Automattic — 1 operation(s) for jetpack-about.
  name: Automattic Jetpack About API
  slug: automattic-jetpack-about-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-active-connected-plugins API from Automattic — 1 operation(s) for jetpack-active-connected-plugins.
  name: Automattic Jetpack Active Connected Plugins API
  slug: automattic-jetpack-active-connected-plugins-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-agency API from Automattic — 8 operation(s) for jetpack-agency.
  name: Automattic Jetpack Agency API
  slug: automattic-jetpack-agency-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-ai API from Automattic — 6 operation(s) for jetpack-ai.
  name: Automattic Jetpack AI API
  slug: automattic-jetpack-ai-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-ai-image API from Automattic — 1 operation(s) for jetpack-ai-image.
  name: Automattic Jetpack AI Image API
  slug: automattic-jetpack-ai-image-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-ai-query API from Automattic — 1 operation(s) for jetpack-ai-query.
  name: Automattic Jetpack AI Query API
  slug: automattic-jetpack-ai-query-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-ai-transcription API from Automattic — 1 operation(s) for jetpack-ai-transcription.
  name: Automattic Jetpack AI Transcription API
  slug: automattic-jetpack-ai-transcription-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack API from Automattic — 2 operation(s) for jetpack.
  name: Automattic Jetpack API
  slug: automattic-jetpack-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-boost API from Automattic — 13 operation(s) for jetpack-boost.
  name: Automattic Jetpack Boost API
  slug: automattic-jetpack-boost-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-boost-proxy API from Automattic — 4 operation(s) for jetpack-boost-proxy.
  name: Automattic Jetpack Boost Proxy API
  slug: automattic-jetpack-boost-proxy-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-clone-settings API from Automattic — 1 operation(s) for jetpack-clone-settings.
  name: Automattic Jetpack Clone Settings API
  slug: automattic-jetpack-clone-settings-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-connect API from Automattic — 1 operation(s) for jetpack-connect.
  name: Automattic Jetpack Connect API
  slug: automattic-jetpack-connect-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-connection-health API from Automattic — 1 operation(s) for jetpack-connection-health.
  name: Automattic Jetpack Connection Health API
  slug: automattic-jetpack-connection-health-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-forms API from Automattic — 8 operation(s) for jetpack-forms.
  name: Automattic Jetpack Forms API
  slug: automattic-jetpack-forms-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-global-styles API from Automattic — 1 operation(s) for jetpack-global-styles.
  name: Automattic Jetpack Global Styles API
  slug: automattic-jetpack-global-styles-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-golden-token API from Automattic — 2 operation(s) for jetpack-golden-token.
  name: Automattic Jetpack Golden Token API
  slug: automattic-jetpack-golden-token-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-licensing API from Automattic — 24 operation(s) for jetpack-licensing.
  name: Automattic Jetpack Licensing API
  slug: automattic-jetpack-licensing-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-manage API from Automattic — 2 operation(s) for jetpack-manage.
  name: Automattic Jetpack Manage API
  slug: automattic-jetpack-manage-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-marketing API from Automattic — 2 operation(s) for jetpack-marketing.
  name: Automattic Jetpack Marketing API
  slug: automattic-jetpack-marketing-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-monitor-incidents API from Automattic — 1 operation(s) for jetpack-monitor-incidents.
  name: Automattic Jetpack Monitor Incidents API
  slug: automattic-jetpack-monitor-incidents-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-monitor-settings API from Automattic — 2 operation(s) for jetpack-monitor-settings.
  name: Automattic Jetpack Monitor Settings API
  slug: automattic-jetpack-monitor-settings-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-monitor-status API from Automattic — 1 operation(s) for jetpack-monitor-status.
  name: Automattic Jetpack Monitor Status API
  slug: automattic-jetpack-monitor-status-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-monitor-uptime API from Automattic — 1 operation(s) for jetpack-monitor-uptime.
  name: Automattic Jetpack Monitor Uptime API
  slug: automattic-jetpack-monitor-uptime-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-openai-query API from Automattic — 1 operation(s) for jetpack-openai-query.
  name: Automattic Jetpack Openai Query API
  slug: automattic-jetpack-openai-query-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-package-versions API from Automattic — 1 operation(s) for jetpack-package-versions.
  name: Automattic Jetpack Package Versions API
  slug: automattic-jetpack-package-versions-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-partner API from Automattic — 4 operation(s) for jetpack-partner.
  name: Automattic Jetpack Partner API
  slug: automattic-jetpack-partner-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-partners API from Automattic — 14 operation(s) for jetpack-partners.
  name: Automattic Jetpack Partners API
  slug: automattic-jetpack-partners-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-pinghub API from Automattic — 1 operation(s) for jetpack-pinghub.
  name: Automattic Jetpack Pinghub API
  slug: automattic-jetpack-pinghub-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-product-data API from Automattic — 1 operation(s) for jetpack-product-data.
  name: Automattic Jetpack Product Data API
  slug: automattic-jetpack-product-data-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-protect-global-stats API from Automattic — 1 operation(s) for jetpack-protect-global-stats.
  name: Automattic Jetpack Protect Global Stats API
  slug: automattic-jetpack-protect-global-stats-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-protect-send-verification-code API from Automattic — 1 operation(s) for jetpack-protect-send-verification-code.
  name: Automattic Jetpack Protect Send Verification Code API
  slug: automattic-jetpack-protect-send-verification-code-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-protect-status API from Automattic — 1 operation(s) for jetpack-protect-status.
  name: Automattic Jetpack Protect Status API
  slug: automattic-jetpack-protect-status-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-protect-weak-password API from Automattic — 1 operation(s) for jetpack-protect-weak-password.
  name: Automattic Jetpack Protect Weak Password API
  slug: automattic-jetpack-protect-weak-password-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-recommendations API from Automattic — 4 operation(s) for jetpack-recommendations.
  name: Automattic Jetpack Recommendations API
  slug: automattic-jetpack-recommendations-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-refresh-blog-token API from Automattic — 1 operation(s) for jetpack-refresh-blog-token.
  name: Automattic Jetpack Refresh Blog Token API
  slug: automattic-jetpack-refresh-blog-token-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-remote-connect-user API from Automattic — 1 operation(s) for jetpack-remote-connect-user.
  name: Automattic Jetpack Remote Connect User API
  slug: automattic-jetpack-remote-connect-user-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-report-error API from Automattic — 1 operation(s) for jetpack-report-error.
  name: Automattic Jetpack Report Error API
  slug: automattic-jetpack-report-error-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-search API from Automattic — 6 operation(s) for jetpack-search.
  name: Automattic Jetpack Search API
  slug: automattic-jetpack-search-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-social API from Automattic — 2 operation(s) for jetpack-social.
  name: Automattic Jetpack Social API
  slug: automattic-jetpack-social-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-start-webhooks API from Automattic — 1 operation(s) for jetpack-start-webhooks.
  name: Automattic Jetpack Start Webhooks API
  slug: automattic-jetpack-start-webhooks-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-stats API from Automattic — 2 operation(s) for jetpack-stats.
  name: Automattic Jetpack Stats API
  slug: automattic-jetpack-stats-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-stats-dashboard API from Automattic — 3 operation(s) for jetpack-stats-dashboard.
  name: Automattic Jetpack Stats Dashboard API
  slug: automattic-jetpack-stats-dashboard-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-sync-actions API from Automattic — 1 operation(s) for jetpack-sync-actions.
  name: Automattic Jetpack Sync Actions API
  slug: automattic-jetpack-sync-actions-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-token-health API from Automattic — 3 operation(s) for jetpack-token-health.
  name: Automattic Jetpack Token Health API
  slug: automattic-jetpack-token-health-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-user-attributes API from Automattic — 1 operation(s) for jetpack-user-attributes.
  name: Automattic Jetpack User Attributes API
  slug: automattic-jetpack-user-attributes-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-user-tracking API from Automattic — 1 operation(s) for jetpack-user-tracking.
  name: Automattic Jetpack User Tracking API
  slug: automattic-jetpack-user-tracking-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jetpack-wpcom-user-data API from Automattic — 1 operation(s) for jetpack-wpcom-user-data.
  name: Automattic Jetpack Wpcom User Data API
  slug: automattic-jetpack-wpcom-user-data-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jitm API from Automattic — 1 operation(s) for jitm.
  name: Automattic Jitm API
  slug: automattic-jitm-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jp_pay_order API from Automattic — 4 operation(s) for jp_pay_order.
  name: Automattic Jp Pay Order API
  slug: automattic-jp-pay-order-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jp_pay_product API from Automattic — 4 operation(s) for jp_pay_product.
  name: Automattic Jp Pay Product API
  slug: automattic-jp-pay-product-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The jurassic-ninja API from Automattic — 8 operation(s) for jurassic-ninja.
  name: Automattic Jurassic Ninja API
  slug: automattic-jurassic-ninja-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: Check which sites use your API key and how many requests are being made
  name: Automattic Key Usage API
  slug: automattic-key-usage-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: Verify Akismet API key
  name: Automattic Key Verification API
  slug: automattic-key-verification-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The knowledge API from Automattic — 7 operation(s) for knowledge.
  name: Automattic Knowledge API
  slug: automattic-knowledge-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The lasagna API from Automattic — 1 operation(s) for lasagna.
  name: Automattic Lasagna API
  slug: automattic-lasagna-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The launch API from Automattic — 1 operation(s) for launch.
  name: Automattic Launch API
  slug: automattic-launch-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The launch-site API from Automattic — 1 operation(s) for launch-site.
  name: Automattic Launch Site API
  slug: automattic-launch-site-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The launchpad API from Automattic — 2 operation(s) for launchpad.
  name: Automattic Launchpad API
  slug: automattic-launchpad-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The legal API from Automattic — 1 operation(s) for legal.
  name: Automattic Legal API
  slug: automattic-legal-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The liked-posts API from Automattic — 1 operation(s) for liked-posts.
  name: Automattic Liked Posts API
  slug: automattic-liked-posts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The linear-solver API from Automattic — 8 operation(s) for linear-solver.
  name: Automattic Linear Solver API
  slug: automattic-linear-solver-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The linearmattic API from Automattic — 2 operation(s) for linearmattic.
  name: Automattic Linearmattic API
  slug: automattic-linearmattic-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The mailchimp API from Automattic — 3 operation(s) for mailchimp.
  name: Automattic Mailchimp API
  slug: automattic-mailchimp-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The mailpoet API from Automattic — 1 operation(s) for mailpoet.
  name: Automattic Mailpoet API
  slug: automattic-mailpoet-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The manual-payments API from Automattic — 2 operation(s) for manual-payments.
  name: Automattic Manual Payments API
  slug: automattic-manual-payments-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The mapbox API from Automattic — 1 operation(s) for mapbox.
  name: Automattic Mapbox API
  slug: automattic-mapbox-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The mapkit API from Automattic — 1 operation(s) for mapkit.
  name: Automattic Mapkit API
  slug: automattic-mapkit-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The marketing API from Automattic — 2 operation(s) for marketing.
  name: Automattic Marketing API
  slug: automattic-marketing-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The marketplace API from Automattic — 20 operation(s) for marketplace.
  name: Automattic Marketplace API
  slug: automattic-marketplace-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The mcp-abilities API from Automattic — 1 operation(s) for mcp-abilities.
  name: Automattic MCP Abilities API
  slug: automattic-mcp-abilities-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The me API from Automattic — 17 operation(s) for me.
  name: Automattic Me API
  slug: automattic-me-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The media API from Automattic — 14 operation(s) for media.
  name: Automattic Media API
  slug: automattic-media-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The memberships API from Automattic — 10 operation(s) for memberships.
  name: Automattic Memberships API
  slug: automattic-memberships-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The menu-items API from Automattic — 4 operation(s) for menu-items.
  name: Automattic Menu Items API
  slug: automattic-menu-items-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The menu-locations API from Automattic — 2 operation(s) for menu-locations.
  name: Automattic Menu Locations API
  slug: automattic-menu-locations-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The menus API from Automattic — 6 operation(s) for menus.
  name: Automattic Menus API
  slug: automattic-menus-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The meta API from Automattic — 6 operation(s) for meta.
  name: Automattic Meta API
  slug: automattic-meta-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The migrate-from API from Automattic — 1 operation(s) for migrate-from.
  name: Automattic Migrate From API
  slug: automattic-migrate-from-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The migrate-provision API from Automattic — 1 operation(s) for migrate-provision.
  name: Automattic Migrate Provision API
  slug: automattic-migrate-provision-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The migration-enabled API from Automattic — 1 operation(s) for migration-enabled.
  name: Automattic Migration Enabled API
  slug: automattic-migration-enabled-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The migration-flow API from Automattic — 1 operation(s) for migration-flow.
  name: Automattic Migration Flow API
  slug: automattic-migration-flow-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The migration-provider-notifications API from Automattic — 1 operation(s) for migration-provider-notifications.
  name: Automattic Migration Provider Notifications API
  slug: automattic-migration-provider-notifications-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The migration-provider-redirect API from Automattic — 1 operation(s) for migration-provider-redirect.
  name: Automattic Migration Provider Redirect API
  slug: automattic-migration-provider-redirect-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The migration-status API from Automattic — 1 operation(s) for migration-status.
  name: Automattic Migration Status API
  slug: automattic-migration-status-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The migrations API from Automattic — 2 operation(s) for migrations.
  name: Automattic Migrations API
  slug: automattic-migrations-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The mobile API from Automattic — 6 operation(s) for mobile.
  name: Automattic Mobile API
  slug: automattic-mobile-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The mobile-support API from Automattic — 6 operation(s) for mobile-support.
  name: Automattic Mobile Support API
  slug: automattic-mobile-support-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The navigation API from Automattic — 6 operation(s) for navigation.
  name: Automattic Navigation API
  slug: automattic-navigation-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The newsletter-categories API from Automattic — 5 operation(s) for newsletter-categories.
  name: Automattic Newsletter Categories API
  slug: automattic-newsletter-categories-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The newsletter-email-sent-status API from Automattic — 1 operation(s) for newsletter-email-sent-status.
  name: Automattic Newsletter Email Sent Status API
  slug: automattic-newsletter-email-sent-status-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The newspack-blocks-posts API from Automattic — 1 operation(s) for newspack-blocks-posts.
  name: Automattic Newspack Blocks Posts API
  slug: automattic-newspack-blocks-posts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The newspack-blocks-specific-posts API from Automattic — 1 operation(s) for newspack-blocks-specific-posts.
  name: Automattic Newspack Blocks Specific Posts API
  slug: automattic-newspack-blocks-specific-posts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The newspack-gpt API from Automattic — 1 operation(s) for newspack-gpt.
  name: Automattic Newspack Gpt API
  slug: automattic-newspack-gpt-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The newspack-manager API from Automattic — 1 operation(s) for newspack-manager.
  name: Automattic Newspack Manager API
  slug: automattic-newspack-manager-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The notifications API from Automattic — 3 operation(s) for notifications.
  name: Automattic Notifications API
  slug: automattic-notifications-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The nudge API from Automattic — 1 operation(s) for nudge.
  name: Automattic Nudge API
  slug: automattic-nudge-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The oauth2 API from Automattic — 1 operation(s) for oauth2.
  name: Automattic Oauth2 API
  slug: automattic-oauth2-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The odie API from Automattic — 5 operation(s) for odie.
  name: Automattic Odie API
  slug: automattic-odie-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The odie-search API from Automattic — 1 operation(s) for odie-search.
  name: Automattic Odie Search API
  slug: automattic-odie-search-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The oembed-proxy API from Automattic — 2 operation(s) for oembed-proxy.
  name: Automattic Oembed Proxy API
  slug: automattic-oembed-proxy-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The onboarding API from Automattic — 1 operation(s) for onboarding.
  name: Automattic Onboarding API
  slug: automattic-onboarding-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The onboarding-customization API from Automattic — 1 operation(s) for onboarding-customization.
  name: Automattic Onboarding Customization API
  slug: automattic-onboarding-customization-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The p2 API from Automattic — 2 operation(s) for p2.
  name: Automattic P2 API
  slug: automattic-p2-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The pages API from Automattic — 6 operation(s) for pages.
  name: Automattic Pages API
  slug: automattic-pages-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The pagespeed API from Automattic — 1 operation(s) for pagespeed.
  name: Automattic Pagespeed API
  slug: automattic-pagespeed-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The partners API from Automattic — 1 operation(s) for partners.
  name: Automattic Partners API
  slug: automattic-partners-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The pattern-assembler API from Automattic — 6 operation(s) for pattern-assembler.
  name: Automattic Pattern Assembler API
  slug: automattic-pattern-assembler-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The pattern-directory API from Automattic — 1 operation(s) for pattern-directory.
  name: Automattic Pattern Directory API
  slug: automattic-pattern-directory-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The pending-blog-subscriptions API from Automattic — 3 operation(s) for pending-blog-subscriptions.
  name: Automattic Pending Blog Subscriptions API
  slug: automattic-pending-blog-subscriptions-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The people API from Automattic — 2 operation(s) for people.
  name: Automattic People API
  slug: automattic-people-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The photodna API from Automattic — 1 operation(s) for photodna.
  name: Automattic Photodna API
  slug: automattic-photodna-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The pigeon API from Automattic — 2 operation(s) for pigeon.
  name: Automattic Pigeon API
  slug: automattic-pigeon-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The plans API from Automattic — 4 operation(s) for plans.
  name: Automattic Plans API
  slug: automattic-plans-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The playground API from Automattic — 2 operation(s) for playground.
  name: Automattic Playground API
  slug: automattic-playground-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The plugins API from Automattic — 4 operation(s) for plugins.
  name: Automattic Plugins API
  slug: automattic-plugins-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The podcast API from Automattic — 1 operation(s) for podcast.
  name: Automattic Podcast API
  slug: automattic-podcast-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The podcast-distribution API from Automattic — 1 operation(s) for podcast-distribution.
  name: Automattic Podcast Distribution API
  slug: automattic-podcast-distribution-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The podcast-player API from Automattic — 2 operation(s) for podcast-player.
  name: Automattic Podcast Player API
  slug: automattic-podcast-player-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The podcast-stats API from Automattic — 4 operation(s) for podcast-stats.
  name: Automattic Podcast Stats API
  slug: automattic-podcast-stats-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The portfolio-dashboard-agent API from Automattic — 2 operation(s) for portfolio-dashboard-agent.
  name: Automattic Portfolio Dashboard Agent API
  slug: automattic-portfolio-dashboard-agent-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The post-comment-subscriptions API from Automattic — 4 operation(s) for post-comment-subscriptions.
  name: Automattic Post Comment Subscriptions API
  slug: automattic-post-comment-subscriptions-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The post-counts API from Automattic — 1 operation(s) for post-counts.
  name: Automattic Post Counts API
  slug: automattic-post-counts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The post-types API from Automattic — 1 operation(s) for post-types.
  name: Automattic Post Types API
  slug: automattic-post-types-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The posts API from Automattic — 34 operation(s) for posts.
  name: Automattic Posts API
  slug: automattic-posts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The posts-to-podcast API from Automattic — 4 operation(s) for posts-to-podcast.
  name: Automattic Posts To Podcast API
  slug: automattic-posts-to-podcast-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The presales API from Automattic — 1 operation(s) for presales.
  name: Automattic Presales API
  slug: automattic-presales-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The preview-links API from Automattic — 2 operation(s) for preview-links.
  name: Automattic Preview Links API
  slug: automattic-preview-links-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The pricing-dashboard API from Automattic — 5 operation(s) for pricing-dashboard.
  name: Automattic Pricing Dashboard API
  slug: automattic-pricing-dashboard-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The privacy-policy API from Automattic — 2 operation(s) for privacy-policy.
  name: Automattic Privacy Policy API
  slug: automattic-privacy-policy-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The private API from Automattic — 1 operation(s) for private.
  name: Automattic Private API
  slug: automattic-private-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The private-podcasts API from Automattic — 4 operation(s) for private-podcasts.
  name: Automattic Private Podcasts API
  slug: automattic-private-podcasts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The products API from Automattic — 1 operation(s) for products.
  name: Automattic Products API
  slug: automattic-products-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The profile API from Automattic — 1 operation(s) for profile.
  name: Automattic Profile API
  slug: automattic-profile-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The protect API from Automattic — 3 operation(s) for protect.
  name: Automattic Protect API
  slug: automattic-protect-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The publicize API from Automattic — 15 operation(s) for publicize.
  name: Automattic Publicize API
  slug: automattic-publicize-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The push-notifications API from Automattic — 1 operation(s) for push-notifications.
  name: Automattic Push Notifications API
  slug: automattic-push-notifications-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The read API from Automattic — 52 operation(s) for read.
  name: Automattic Read API
  slug: automattic-read-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The reader API from Automattic — 106 operation(s) for reader.
  name: Automattic Reader API
  slug: automattic-reader-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The reader-chat-settings API from Automattic — 1 operation(s) for reader-chat-settings.
  name: Automattic Reader Chat Settings API
  slug: automattic-reader-chat-settings-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The recovery-mode-status API from Automattic — 1 operation(s) for recovery-mode-status.
  name: Automattic Recovery Mode Status API
  slug: automattic-recovery-mode-status-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The related-posts API from Automattic — 3 operation(s) for related-posts.
  name: Automattic Related Posts API
  slug: automattic-related-posts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The reset-migration API from Automattic — 1 operation(s) for reset-migration.
  name: Automattic Reset Migration API
  slug: automattic-reset-migration-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The reset-site API from Automattic — 3 operation(s) for reset-site.
  name: Automattic Reset Site API
  slug: automattic-reset-site-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The restore-site API from Automattic — 1 operation(s) for restore-site.
  name: Automattic Restore Site API
  slug: automattic-restore-site-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The rewind API from Automattic — 34 operation(s) for rewind.
  name: Automattic Rewind API
  slug: automattic-rewind-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The rtc API from Automattic — 2 operation(s) for rtc.
  name: Automattic Rtc API
  slug: automattic-rtc-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The rtc-notices API from Automattic — 3 operation(s) for rtc-notices.
  name: Automattic Rtc Notices API
  slug: automattic-rtc-notices-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The scan API from Automattic — 5 operation(s) for scan.
  name: Automattic Scan API
  slug: automattic-scan-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The scheduled-updates API from Automattic — 2 operation(s) for scheduled-updates.
  name: Automattic Scheduled Updates API
  slug: automattic-scheduled-updates-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The search API from Automattic — 1 operation(s) for search.
  name: Automattic Search API
  slug: automattic-search-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The search-stats API from Automattic — 1 operation(s) for search-stats.
  name: Automattic Search Stats API
  slug: automattic-search-stats-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The search-suggestions API from Automattic — 1 operation(s) for search-suggestions.
  name: Automattic Search Suggestions API
  slug: automattic-search-suggestions-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The seen-posts API from Automattic — 6 operation(s) for seen-posts.
  name: Automattic Seen Posts API
  slug: automattic-seen-posts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The segmentation-survey API from Automattic — 4 operation(s) for segmentation-survey.
  name: Automattic Segmentation Survey API
  slug: automattic-segmentation-survey-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The segments API from Automattic — 1 operation(s) for segments.
  name: Automattic Segments API
  slug: automattic-segments-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The seller_footer API from Automattic — 1 operation(s) for seller_footer.
  name: Automattic Seller Footer API
  slug: automattic-seller-footer-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The send API from Automattic — 3 operation(s) for send.
  name: Automattic Send API
  slug: automattic-send-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The send-email-continue-site-build API from Automattic — 1 operation(s) for send-email-continue-site-build.
  name: Automattic Send Email Continue Site Build API
  slug: automattic-send-email-continue-site-build-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The send-email-preview API from Automattic — 1 operation(s) for send-email-preview.
  name: Automattic Send Email Preview API
  slug: automattic-send-email-preview-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The service-api-keys API from Automattic — 1 operation(s) for service-api-keys.
  name: Automattic Service API Keys API
  slug: automattic-service-api-keys-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The settings API from Automattic — 1 operation(s) for settings.
  name: Automattic Settings API
  slug: automattic-settings-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The shares-count API from Automattic — 1 operation(s) for shares-count.
  name: Automattic Shares Count API
  slug: automattic-shares-count-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The sharing API from Automattic — 15 operation(s) for sharing.
  name: Automattic Sharing API
  slug: automattic-sharing-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The shipstation API from Automattic — 1 operation(s) for shipstation.
  name: Automattic Shipstation API
  slug: automattic-shipstation-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The sidebars API from Automattic — 2 operation(s) for sidebars.
  name: Automattic Sidebars API
  slug: automattic-sidebars-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The simple-payments API from Automattic — 2 operation(s) for simple-payments.
  name: Automattic Simple Payments API
  slug: automattic-simple-payments-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site API from Automattic — 5 operation(s) for site.
  name: Automattic Site API
  slug: automattic-site-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-assembler API from Automattic — 1 operation(s) for site-assembler.
  name: Automattic Site Assembler API
  slug: automattic-site-assembler-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-goals API from Automattic — 1 operation(s) for site-goals.
  name: Automattic Site Goals API
  slug: automattic-site-goals-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-has-never-published-post API from Automattic — 1 operation(s) for site-has-never-published-post.
  name: Automattic Site Has Never Published Post API
  slug: automattic-site-has-never-published-post-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-importer API from Automattic — 5 operation(s) for site-importer.
  name: Automattic Site Importer API
  slug: automattic-site-importer-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-intent API from Automattic — 1 operation(s) for site-intent.
  name: Automattic Site Intent API
  slug: automattic-site-intent-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-migration-status-sticker API from Automattic — 1 operation(s) for site-migration-status-sticker.
  name: Automattic Site Migration Status Sticker API
  slug: automattic-site-migration-status-sticker-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-owner-transfer API from Automattic — 3 operation(s) for site-owner-transfer.
  name: Automattic Site Owner Transfer API
  slug: automattic-site-owner-transfer-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-suggestions API from Automattic — 1 operation(s) for site-suggestions.
  name: Automattic Site Suggestions API
  slug: automattic-site-suggestions-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-type API from Automattic — 1 operation(s) for site-type.
  name: Automattic Site Type API
  slug: automattic-site-type-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The site-vertical API from Automattic — 1 operation(s) for site-vertical.
  name: Automattic Site Vertical API
  slug: automattic-site-vertical-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The sites API from Automattic — 25 operation(s) for sites.
  name: Automattic Sites API
  slug: automattic-sites-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The slack API from Automattic — 1 operation(s) for slack.
  name: Automattic Slack API
  slug: automattic-slack-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: Check for spam, and submit spam or ham (false positives)
  name: Automattic Spam API
  slug: automattic-spam-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The ssh-migration API from Automattic — 5 operation(s) for ssh-migration.
  name: Automattic Ssh Migration API
  slug: automattic-ssh-migration-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The staging-site API from Automattic — 7 operation(s) for staging-site.
  name: Automattic Staging Site API
  slug: automattic-staging-site-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The starter-designs API from Automattic — 2 operation(s) for starter-designs.
  name: Automattic Starter Designs API
  slug: automattic-starter-designs-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The stats API from Automattic — 43 operation(s) for stats.
  name: Automattic Stats API
  slug: automattic-stats-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The statuses API from Automattic — 2 operation(s) for statuses.
  name: Automattic Statuses API
  slug: automattic-statuses-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The studio-app API from Automattic — 14 operation(s) for studio-app.
  name: Automattic Studio App API
  slug: automattic-studio-app-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The subscribers API from Automattic — 19 operation(s) for subscribers.
  name: Automattic Subscribers API
  slug: automattic-subscribers-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The subscribers_by_user_type API from Automattic — 1 operation(s) for subscribers_by_user_type.
  name: Automattic Subscribers By User Type API
  slug: automattic-subscribers-by-user-type-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The support-interactions API from Automattic — 4 operation(s) for support-interactions.
  name: Automattic Support Interactions API
  slug: automattic-support-interactions-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The supportforums API from Automattic — 1 operation(s) for supportforums.
  name: Automattic Supportforums API
  slug: automattic-supportforums-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The sync API from Automattic — 1 operation(s) for sync.
  name: Automattic Sync API
  slug: automattic-sync-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The tags API from Automattic — 3 operation(s) for tags.
  name: Automattic Tags API
  slug: automattic-tags-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The taxonomies API from Automattic — 2 operation(s) for taxonomies.
  name: Automattic Taxonomies API
  slug: automattic-taxonomies-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The taxonomy API from Automattic — 13 operation(s) for taxonomy.
  name: Automattic Taxonomy API
  slug: automattic-taxonomy-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The telegram-bot API from Automattic — 8 operation(s) for telegram-bot.
  name: Automattic Telegram Bot API
  slug: automattic-telegram-bot-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The template-loader API from Automattic — 1 operation(s) for template-loader.
  name: Automattic Template Loader API
  slug: automattic-template-loader-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The template-parts API from Automattic — 7 operation(s) for template-parts.
  name: Automattic Template Parts API
  slug: automattic-template-parts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The templates API from Automattic — 7 operation(s) for templates.
  name: Automattic Templates API
  slug: automattic-templates-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The test API from Automattic — 1 operation(s) for test.
  name: Automattic Test API
  slug: automattic-test-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The tests API from Automattic — 3 operation(s) for tests.
  name: Automattic Tests API
  slug: automattic-tests-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The text-completion API from Automattic — 2 operation(s) for text-completion.
  name: Automattic Text Completion API
  slug: automattic-text-completion-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The theme-headstart API from Automattic — 1 operation(s) for theme-headstart.
  name: Automattic Theme Headstart API
  slug: automattic-theme-headstart-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The theme-setup API from Automattic — 1 operation(s) for theme-setup.
  name: Automattic Theme Setup API
  slug: automattic-theme-setup-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The theme-support API from Automattic — 1 operation(s) for theme-support.
  name: Automattic Theme Support API
  slug: automattic-theme-support-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The themes API from Automattic — 11 operation(s) for themes.
  name: Automattic Themes API
  slug: automattic-themes-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The timezones API from Automattic — 1 operation(s) for timezones.
  name: Automattic Timezones API
  slug: automattic-timezones-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The titan API from Automattic — 1 operation(s) for titan.
  name: Automattic Titan API
  slug: automattic-titan-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The top-posts API from Automattic — 1 operation(s) for top-posts.
  name: Automattic Top Posts API
  slug: automattic-top-posts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The tortuga API from Automattic — 1 operation(s) for tortuga.
  name: Automattic Tortuga API
  slug: automattic-tortuga-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The traffic-guide-download API from Automattic — 1 operation(s) for traffic-guide-download.
  name: Automattic Traffic Guide Download API
  slug: automattic-traffic-guide-download-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The transfer API from Automattic — 1 operation(s) for transfer.
  name: Automattic Transfer API
  slug: automattic-transfer-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The transients API from Automattic — 1 operation(s) for transients.
  name: Automattic Transients API
  slug: automattic-transients-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The trelloCallback API from Automattic — 1 operation(s) for trellocallback.
  name: Automattic Trello Callback API
  slug: automattic-trellocallback-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The trends-agent API from Automattic — 3 operation(s) for trends-agent.
  name: Automattic Trends Agent API
  slug: automattic-trends-agent-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The tumblr-smtp API from Automattic — 1 operation(s) for tumblr-smtp.
  name: Automattic Tumblr Smtp API
  slug: automattic-tumblr-smtp-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The twilio-notification API from Automattic — 1 operation(s) for twilio-notification.
  name: Automattic Twilio Notification API
  slug: automattic-twilio-notification-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The twitter API from Automattic — 1 operation(s) for twitter.
  name: Automattic Twitter API
  slug: automattic-twitter-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The typekit-fonts API from Automattic — 5 operation(s) for typekit-fonts.
  name: Automattic Typekit Fonts API
  slug: automattic-typekit-fonts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The types API from Automattic — 2 operation(s) for types.
  name: Automattic Types API
  slug: automattic-types-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The ucp API from Automattic — 15 operation(s) for ucp.
  name: Automattic Ucp API
  slug: automattic-ucp-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The unauth-file-upload API from Automattic — 4 operation(s) for unauth-file-upload.
  name: Automattic Unauth File Upload API
  slug: automattic-unauth-file-upload-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The update-schedules API from Automattic — 5 operation(s) for update-schedules.
  name: Automattic Update Schedules API
  slug: automattic-update-schedules-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The upgrades API from Automattic — 1 operation(s) for upgrades.
  name: Automattic Upgrades API
  slug: automattic-upgrades-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The user-type API from Automattic — 1 operation(s) for user-type.
  name: Automattic User Type API
  slug: automattic-user-type-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The users API from Automattic — 27 operation(s) for users.
  name: Automattic Users API
  slug: automattic-users-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The verticals API from Automattic — 5 operation(s) for verticals.
  name: Automattic Verticals API
  slug: automattic-verticals-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The vibehost API from Automattic — 3 operation(s) for vibehost.
  name: Automattic Vibehost API
  slug: automattic-vibehost-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The videopress API from Automattic — 9 operation(s) for videopress.
  name: Automattic Videopress API
  slug: automattic-videopress-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The videos API from Automattic — 7 operation(s) for videos.
  name: Automattic Videos API
  slug: automattic-videos-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The view-config API from Automattic — 1 operation(s) for view-config.
  name: Automattic View Config API
  slug: automattic-view-config-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The vip API from Automattic — 2 operation(s) for vip.
  name: Automattic Vip API
  slug: automattic-vip-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The vouchers API from Automattic — 3 operation(s) for vouchers.
  name: Automattic Vouchers API
  slug: automattic-vouchers-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The waf-rules API from Automattic — 1 operation(s) for waf-rules.
  name: Automattic Waf Rules API
  slug: automattic-waf-rules-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wc API from Automattic — 20 operation(s) for wc.
  name: Automattic Wc API
  slug: automattic-wc-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wcai-pa API from Automattic — 6 operation(s) for wcai-pa.
  name: Automattic Wcai Pa API
  slug: automattic-wcai-pa-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wcbazaar API from Automattic — 9 operation(s) for wcbazaar.
  name: Automattic Wcbazaar API
  slug: automattic-wcbazaar-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wccom API from Automattic — 4 operation(s) for wccom.
  name: Automattic Wccom API
  slug: automattic-wccom-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The webhook-airtable-create API from Automattic — 3 operation(s) for webhook-airtable-create.
  name: Automattic Webhook Airtable Create API
  slug: automattic-webhook-airtable-create-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The whats-new API from Automattic — 2 operation(s) for whats-new.
  name: Automattic Whats New API
  slug: automattic-whats-new-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The widget-modules API from Automattic — 1 operation(s) for widget-modules.
  name: Automattic Widget Modules API
  slug: automattic-widget-modules-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The widget-types API from Automattic — 4 operation(s) for widget-types.
  name: Automattic Widget Types API
  slug: automattic-widget-types-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The widgets API from Automattic — 2 operation(s) for widgets.
  name: Automattic Widgets API
  slug: automattic-widgets-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The woo API from Automattic — 3 operation(s) for woo.
  name: Automattic Woo API
  slug: automattic-woo-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The woo-mobile-ai API from Automattic — 1 operation(s) for woo-mobile-ai.
  name: Automattic Woo Mobile AI API
  slug: automattic-woo-mobile-ai-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The woocommerce API from Automattic — 5 operation(s) for woocommerce.
  name: Automattic Woocommerce API
  slug: automattic-woocommerce-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wordads API from Automattic — 5 operation(s) for wordads.
  name: Automattic Wordads API
  slug: automattic-wordads-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wordcamp-coupons API from Automattic — 1 operation(s) for wordcamp-coupons.
  name: Automattic Wordcamp Coupons API
  slug: automattic-wordcamp-coupons-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The work-with-us API from Automattic — 2 operation(s) for work-with-us.
  name: Automattic Work With Us API
  slug: automattic-work-with-us-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wp-abilities API from Automattic — 5 operation(s) for wp-abilities.
  name: Automattic Wp Abilities API
  slug: automattic-wp-abilities-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wp-admin-sidebar API from Automattic — 1 operation(s) for wp-admin-sidebar.
  name: Automattic Wp Admin Sidebar API
  slug: automattic-wp-admin-sidebar-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wp_guideline_type API from Automattic — 2 operation(s) for wp_guideline_type.
  name: Automattic Wp Guideline Type API
  slug: automattic-wp-guideline-type-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wp_knowledge_type API from Automattic — 2 operation(s) for wp_knowledge_type.
  name: Automattic Wp Knowledge Type API
  slug: automattic-wp-knowledge-type-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wp_pattern_category API from Automattic — 2 operation(s) for wp_pattern_category.
  name: Automattic Wp Pattern Category API
  slug: automattic-wp-pattern-category-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wp-v2 API from Automattic — 2 operation(s) for wp-v2.
  name: Automattic Wp V2 API
  slug: automattic-wp-v2-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The Wpcom API from Automattic — 3 operation(s) for wpcom.
  name: Automattic Wpcom API
  slug: automattic-wpcom-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wpcom-v2 API from Automattic — 2 operation(s) for wpcom-v2.
  name: Automattic Wpcom V2 API
  slug: automattic-wpcom-v2-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The wrangler API from Automattic — 2 operation(s) for wrangler.
  name: Automattic Wrangler API
  slug: automattic-wrangler-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The xposts API from Automattic — 1 operation(s) for xposts.
  name: Automattic Xposts API
  slug: automattic-xposts-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The zendesk API from Automattic — 1 operation(s) for zendesk.
  name: Automattic Zendesk API
  slug: automattic-zendesk-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The zendesk-notification API from Automattic — 9 operation(s) for zendesk-notification.
  name: Automattic Zendesk Notification API
  slug: automattic-zendesk-notification-api
- baseURL: https://public-api.wordpress.com/rest/v1.1
  baseurl_source: declared
  description: The zendesk-notification-staging API from Automattic — 1 operation(s) for zendesk-notification-staging.
  name: Automattic Zendesk Notification Staging API
  slug: automattic-zendesk-notification-staging-api
artifact_total: 399
asyncapis:
- description: ''
  name: Automattic Wordpress Com Webhooks
  slug: automattic-wordpress-com-webhooks
collections:
- collection_type: open
  name: Akismet API
  slug: open-automattic-akismet
- collection_type: open
  name: WordPress.com REST API v1.1
  slug: open-automattic-wordpress-com-rest-v1-1
- collection_type: open
  name: WordPress.com REST API v1.2
  slug: open-automattic-wordpress-com-rest-v1-2
- collection_type: open
  name: WordPress.com REST API v1.3
  slug: open-automattic-wordpress-com-rest-v1-3
- collection_type: open
  name: WordPress.com REST API — wp/v2 namespace
  slug: open-automattic-wordpress-com-wp-v2
- collection_type: open
  name: WordPress.com REST API — wpcom/v2 namespace
  slug: open-automattic-wordpress-com-wpcom-v2
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/automattic-wordpress-com-rest-v1-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/automattic-wordpress-com-rest-v1-2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/automattic-wordpress-com-rest-v1-3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/automattic-wordpress-com-wp-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/automattic-wordpress-com-wpcom-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/automattic-akismet-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/automattic-jetpack-ai-plugin-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Automattic/akismet-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Automattic/akismet-api/releases
- group: company
  title: ''
  type: Website
  url: https://automattic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wordpress.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wordpress.com/docs/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wordpress.com/docs/api/rest-api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wordpress.com/docs/api/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://wordpress.com/support/
- group: company
  title: ''
  type: Blog
  url: https://automattic.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Automattic
- group: commercial
  title: ''
  type: Pricing
  url: https://wordpress.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://developer.wordpress.com/apps/new/
- group: start
  title: ''
  type: Login
  url: https://wordpress.com/log-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wordpress.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://automattic.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://automatticstatus.com/
- group: auth
  title: ''
  type: Security
  url: https://automattic.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/automattic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://wpvip.com/trust/
- group: auth
  title: ''
  type: Authentication
  url: authentication/automattic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/automattic-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/automattic-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/automattic-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/automattic-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/automattic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/automattic-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/automattic-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/automattic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/automattic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/automattic-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/automattic-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.wordpress.com/changelog/
- group: design
  title: ''
  type: DataModel
  url: data-model/automattic-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/automattic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/automattic-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/automattic-cli.yml
- group: design
  title: ''
  type: Components
  url: components/automattic-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/automattic-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://developer.wordpress.com/docs/api/console/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/automattic-wordpress-com-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/automattic-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/automattic-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/automattic-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/automattic-tool-crosswalk.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/automattic_stock/
created: '2026-07-31'
description: Automattic is the company behind WordPress.com, Jetpack, WooCommerce, Tumblr, Gravatar, Akismet, WordPress VIP, Pocket Casts, Day One, Beeper and Simplenote. Its developer platform centres on the WordPress.com REST API at public-api.wordpress.com, which serves three parallel namespaces — the WordPress.com-native /rest/v1.x family, the WordPress-core-compatible /wp/v2 family, and the WordPress.com and Jetpack platform extensions in /wpcom/v2 — all behind a single OAuth 2.1 and OpenID Connect authorization server with PKCE, dynamic client registration and resource indicators. Every /rest/ version publishes a machine-readable help document and every /wp/ and /wpcom/ namespace publishes a route index, so the whole surface is self-describing even though Automattic does not ship OpenAPI for it. Automattic also runs a hosted Model Context Protocol server for WordPress.com, publishes OpenAPI for Akismet and for the Jetpack ai-plugin surface, and exposes a GraphQL Platform API for the
  enterprise WordPress VIP product.
image: https://automattic.com/wp-content/uploads/2024/11/cropped-automattic-logo-square.png
layout: provider
mcp_servers:
- description: ''
  name: Automattic MCP Server
  slug: automattic-mcp-server
modified: '2026-07-31'
name: Automattic
nav: Providers
network: true
overview: 'Automattic publishes 383 APIs on the [APIs.io](https://apis.io/) network, including A8c Lore API, A8cmentorship API, Abilities API, and 380 more. Tagged areas include Company, Content Management, Publishing, Blogging, and Website Hosting.


  The Automattic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Automattic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 46 more developer resources.'
random_paper: 12
scopes:
- name: Automattic Scopes
  scope_count: 21
  slug: automattic-scopes
  summary_line: 21 scopes · authorizationCode/refreshToken/clientCredentials
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 25
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.5
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 23.9
    developer_ergonomics: 80.4
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 384
      marker_coverage: 99.0
      total: 388
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/automattic/refs/heads/main/screenshots/automattic-2026-08-07T161958.png
security:
- kind: authentication
  name: Automattic Authentication
  slug: automattic-authentication
  summary_line: oauth2/openIdConnect/http/apiKey · 6 schemes
- kind: domain-security
  name: Automattic Domain Security
  slug: automattic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Automattic Vulnerability Disclosure
  slug: automattic-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Automattic Trust Center
  slug: automattic-trust-center
  summary_line: FedRAMP Moderate, SOC 2 Type I, ISO 27001, SOC 1, GovRAMP, TX-RAMP
slug: automattic
tags:
- Company
- Content Management
- Publishing
- Blogging
- Website Hosting
- Web Publishing
- Content
- Comments
- Spam Filtering
- Media
- Analytics
- Domains
- E-Commerce
- Open-Source
- Developer Tools
- MCP
website: https://automattic.com/
---
