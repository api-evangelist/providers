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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Gitbook Agentic Access
  operation_count: 64
  slug: gitbook-agentic-access
  summary_line: 64 operations · 32 acting
api_count: 1
apis:
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage content within a change request.
  name: GitBook Change Request Content API
  slug: gitbook-change-request-content-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage reviewers for change requests.
  name: GitBook Change Request Reviewers API
  slug: gitbook-change-request-reviewers-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Create, list, review, merge, and update change requests for collaborative editing.
  name: GitBook Change Requests API
  slug: gitbook-change-requests-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Organize and manage grouped sets of spaces.
  name: GitBook Collections API
  slug: gitbook-collections-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Configure custom hostnames for docs sites.
  name: GitBook Custom Hostnames API
  slug: gitbook-custom-hostnames-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Import content into spaces.
  name: GitBook Imports API
  slug: gitbook-imports-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Install and manage third-party integrations.
  name: GitBook Integrations API
  slug: gitbook-integrations-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage members and their roles within an organization.
  name: GitBook Organization Members API
  slug: gitbook-organization-members-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Create and configure organizations to group users, spaces, and collections.
  name: GitBook Organizations API
  slug: gitbook-organizations-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage spaces within a docs site.
  name: GitBook Site Spaces API
  slug: gitbook-site-spaces-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage pages and content within a space.
  name: GitBook Space Content API
  slug: gitbook-space-content-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage spaces which are containers for documentation or knowledge base content.
  name: GitBook Spaces API
  slug: gitbook-spaces-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Resolve and manage content URLs.
  name: GitBook URLs API
  slug: gitbook-urls-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage user accounts and profiles.
  name: GitBook Users API
  slug: gitbook-users-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The agents API from GitBook — 3 operation(s) for agents.
  name: GitBook Agents API
  slug: gitbook-agents-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Centralize billing activities here, including updating payment methods, adjusting subscriptions, or reviewing invoices. Simplify how you track and control costs.
  name: GitBook Billing API
  slug: gitbook-billing-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: This API powers the inline discussion around any new or updated documentation. Participate in comment threads and resolve them after reaching consensus. {% openapi-schemas spec="gitbook" schemas="Comm
  name: GitBook Change Request Comments API
  slug: gitbook-change-request-comments-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Quickly access the full list of collaborators and their contributions within a change request for better traceability and communication. {% openapi-schemas spec="gitbook" schemas="UserContributor" gro
  name: GitBook Change Request Contributors API
  slug: gitbook-change-request-contributors-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The change-request-conversations API from GitBook — 2 operation(s) for change-request-conversations.
  name: GitBook Change Request Conversations API
  slug: gitbook-change-request-conversations-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The change-requests-reviews API from GitBook — 3 operation(s) for change-requests-reviews.
  name: GitBook Change Requests Reviews API
  slug: gitbook-change-requests-reviews-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Control which users and teams have access to a collection's spaces. This ensures only the right individuals can view or modify sensitive content.
  name: GitBook Collection Permissions API
  slug: gitbook-collection-permissions-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The critical API from GitBook — 12 operation(s) for critical.
  name: GitBook Critical API
  slug: gitbook-critical-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Upload and manage custom fonts for branding or aesthetic purposes. Once added, fonts can be applied to your spaces or sites to achieve a unique look. {% openapi-schemas spec="gitbook" schemas="Customi
  name: GitBook Custom Fonts API
  slug: gitbook-custom-fonts-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The git API from GitBook — 9 operation(s) for git.
  name: GitBook Git API
  slug: gitbook-git-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: 'Define terms and specify their translations for different languages to ensure consistent wording. {% openapi-schemas spec="gitbook" schemas="GlossaryEntry" grouped="false" %} The GlossaryEntry object '
  name: GitBook Glossary API
  slug: gitbook-glossary-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Keep a history of your OpenAPI specs, enabling you to compare different versions, revert, or maintain multiple concurrent versions for testing or documentation. {% openapi-schemas spec="gitbook" schem
  name: GitBook Openapi Versions API
  slug: gitbook-openapi-versions-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Enhance your team's knowledge base with the Organization AI ask endpoint, which allows you to query AI models trained on your organization's GitBook content for quick, intelligent responses.
  name: GitBook Organization Ask API
  slug: gitbook-organization-ask-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Use this API to create and revoke invitations for new members. By automating invite flows, you can maintain a cohesive onboarding experience for collaborators and speed up team expansion.
  name: GitBook Organization Invites API
  slug: gitbook-organization-invites-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage the advertisement strategy within your docs. You can specify ad placements, track usage, and adjust settings to best fit your organization's needs.
  name: GitBook Site Ads API
  slug: gitbook-site-ads-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Collect structured feedback from AI agents about the tools, operations, commands and content they worked with, so you can see where agents struggle instead of only how often they call you. Feedback is
  name: GitBook Site Agent Feedback API
  slug: gitbook-site-agent-feedback-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Configure how site issue remediation should behave and provide site-specific instructions for the editing and topic analyst agents. {% openapi-schemas spec="gitbook" schemas="SiteAgentSettings" groupe
  name: GitBook Site Agent Settings API
  slug: gitbook-site-agent-settings-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Build advanced conversational AI experiences within your docs site that go beyond basic Q&A.
  name: GitBook Site AI API
  slug: gitbook-site-ai-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Give your users a way to ask content-aware AI queries that are scoped entirely to the site's published documents.
  name: GitBook Site Ask API
  slug: gitbook-site-ask-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: A site change request groups changes to a site's structure and to the content of any number of its spaces into one review, with a single lifecycle and a single merge decision. {% openapi-schemas spec=
  name: GitBook Site Change Requests API
  slug: gitbook-site-change-requests-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage the channels used as origins for questions and answers in your site ask data. {% openapi-schemas spec="gitbook" schemas="SiteChannel" grouped="false" %} The SiteChannel object {% endopenapi-sch
  name: GitBook Site Channels API
  slug: gitbook-site-channels-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage the contextual records and topics used by your site to power AI experiences and insights. {% openapi-schemas spec="gitbook" schemas="ContextRecord,ContextConnection,SiteTopic,SiteFinding,SiteFi
  name: GitBook Site Context API
  slug: gitbook-site-context-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Update your site's branding, styling, and layout to match your organization's identity. This includes theming elements like color palette, logos, and more. {% openapi-schemas spec="gitbook" schemas="S
  name: GitBook Site Customization API
  slug: gitbook-site-customization-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: External links add absolute HTTP or HTTPS destinations alongside sections and groups in a site's navigation. {% openapi-schemas spec="gitbook" schemas="SiteExternalLink" grouped="false" %} The SiteExt
  name: GitBook Site External Links API
  slug: gitbook-site-external-links-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: This API delivers insights about how visitors interact with your site, including page views and user engagement, helping you measure and optimize your content strategy.
  name: GitBook Site Insights API
  slug: gitbook-site-insights-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage Model Context Protocol (Mcp) servers used by your site. {% openapi-schemas spec="gitbook" schemas="SiteMcpServer" grouped="false" %} The SiteMcpServer object {% endopenapi-schemas %}
  name: GitBook Site MCP Servers API
  slug: gitbook-site-mcp-servers-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Invite, remove, or update users and teams permissions for a site. This provides a way to tightly control collaboration and visibility among your teammates.
  name: GitBook Site Permissions API
  slug: gitbook-site-permissions-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Quickly generate a preview of how your site's content and layout will appear once published, allowing for final checks and refinement prior to going live.
  name: GitBook Site Preview API
  slug: gitbook-site-preview-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Configure the credentials or tokens required to publish documentation externally. This helps ensure your site is consistently kept up to date. {% openapi-schemas spec="gitbook" schemas="SitePublishing
  name: GitBook Site Publishing Auth API
  slug: gitbook-site-publishing-auth-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Inspect the canonical questions asked on your site, the generated answers linked to each question, and the sources used for each answer. {% openapi-schemas spec="gitbook" schemas="SiteQuestion,SiteQue
  name: GitBook Site Questions API
  slug: gitbook-site-questions-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Keep your site's content fresh without breaking old links. This API allows you to create and manage redirection rules. {% openapi-schemas spec="gitbook" schemas="SiteRedirect" grouped="false" %} The S
  name: GitBook Site Redirects API
  slug: gitbook-site-redirects-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Section groups let you bundle multiple top-level sections together, offering additional structuring capabilities and simplifying navigation for your readers. {% openapi-schemas spec="gitbook" schemas=
  name: GitBook Site Section Groups API
  slug: gitbook-site-section-groups-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Sections help partition your site's content at the top level. They can be modified, deleted, or reorganized to reflect your site's changing structure. {% openapi-schemas spec="gitbook" schemas="SiteSe
  name: GitBook Site Sections API
  slug: gitbook-site-sections-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage the lifecycle of share links for your published sites. This includes generating new links for external sharing and revoking or updating existing ones. {% openapi-schemas spec="gitbook" schemas=
  name: GitBook Site Share Links API
  slug: gitbook-site-share-links-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Provides a complete overview of how content is organized on a site. With this API, you can discover page nesting, identify sections, and reorder site elements as needed. {% openapi-schemas spec="gitbo
  name: GitBook Site Structure API
  slug: gitbook-site-structure-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The site-users API from GitBook — 3 operation(s) for site-users.
  name: GitBook Site Users API
  slug: gitbook-site-users-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The Docs Sites API lets you programmatically manage published documentation sites within your organization. You can list and update all sites created under a specific organization, making it easy to a
  name: GitBook Sites API
  slug: gitbook-sites-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The space-comment API from GitBook — 1 operation(s) for space-comment.
  name: GitBook Space Comment API
  slug: gitbook-space-comment-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Comments are a powerful way to gather feedback on your documentation. Use this API to post, list, update, or delete comments and keep conversations organized. {% openapi-schemas spec="gitbook" schemas
  name: GitBook Space Comments API
  slug: gitbook-space-comments-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Automatically fetch metadata or previews for embedded resources such as videos, images, or external docs, enabling richer content experiences in your space.
  name: GitBook Space Embeds API
  slug: gitbook-space-embeds-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Manage the linkage between your GitBook space and external Git repositories, enabling commits, merges, and pull requests directly tied to your documentation.
  name: GitBook Space Git API
  slug: gitbook-space-git-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: This API handles the registration and removal of integrations, automating how data flows between GitBook and your chosen external services.
  name: GitBook Space Integrations API
  slug: gitbook-space-integrations-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Give your collaborators the right level of access for specific spaces, or assign entire teams to your spaces and streamline the process of granting or revoking access at scale, without dealing with in
  name: GitBook Space Permissions API
  slug: gitbook-space-permissions-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Tie GitBook into your corporate identity management and authentication providers (like SAML or OAuth). This centralizes user authentication and improves security. {% openapi-schemas spec="gitbook" sch
  name: GitBook SSO API
  slug: gitbook-sso-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Whether you're hosting images, documents, or other assets, Storage endpoints allow you to integrate those files into your documentation and spaces seamlessly.
  name: GitBook Storage API
  slug: gitbook-storage-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Provide a branded subdomain for each organization to create a consistent user experience. This API supports subdomain creation, DNS checks, and more. {% openapi-schemas spec="gitbook" schemas="Subdoma
  name: GitBook Subdomains API
  slug: gitbook-subdomains-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Use these endpoints to monitor the overall health of GitBook's infrastructure or to retrieve version information for debugging and compliance purposes.
  name: GitBook System API
  slug: gitbook-system-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Easily add or remove users from teams, as well as fine-tune their specific roles within a team to ensure secure, well-organized collaboration. {% openapi-schemas spec="gitbook" schemas="TeamMember" gr
  name: GitBook Team Members API
  slug: gitbook-team-members-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: Teams offer a convenient way to assign roles and access to multiple users at once. This helps maintain large-scale projects more efficiently by reducing overhead in user-by-user management. {% openapi
  name: GitBook Teams API
  slug: gitbook-teams-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The Translations API provides ways to localize your content into various languages. It supports custom strings, default language settings, and more.
  name: GitBook Translations API
  slug: gitbook-translations-api
- baseURL_template: '{host}/v1'
  baseurl_source: spec_template
  description: The OpenAPI endpoints let you integrate your existing or newly generated OpenAPI definitions into GitBook. This includes uploading, updating, and retrieving specs. {% openapi-schemas spec="gitbook" sc
  name: GitBook Open API
  slug: gitbook-open-api-api
artifact_total: 110
asyncapis:
- description: AsyncAPI specification for GitBook webhook events. GitBook emits webhook notifications when key events occur within organizations, spaces, pages, change requests, docs sites, collections, and user acc
  name: GitBook Webhook Events
  slug: gitbook-gitbook-api-asyncapi
- description: ''
  name: Gitbook Webhooks
  slug: gitbook-webhooks
collections:
- collection_type: open
  name: GitBook Change Request Content API
  slug: open-gitbook-change-request-content-api
- collection_type: open
  name: GitBook Change Request Content Change Requests API
  slug: open-gitbook-change-requests-api
- collection_type: open
  name: GitBook Change Request Content Collections API
  slug: open-gitbook-collections-api
- collection_type: open
  name: GitBook Change Request Content Custom Hostnames API
  slug: open-gitbook-custom-hostnames-api
- collection_type: open
  name: GitBook Change Request Content Docs Sites API
  slug: open-gitbook-docs-sites-api
- collection_type: open
  name: GitBook API
  slug: open-gitbook-gitbook-api
- collection_type: open
  name: GitBook Change Request Content Imports API
  slug: open-gitbook-imports-api
- collection_type: open
  name: GitBook Change Request Content Integrations API
  slug: open-gitbook-integrations-api
- collection_type: open
  name: GitBook Change Request Content OpenAPI Specs API
  slug: open-gitbook-openapi-specs-api
- collection_type: open
  name: GitBook Change Request Content Organization Members API
  slug: open-gitbook-organization-members-api
- collection_type: open
  name: GitBook Change Request Content Organization Teams API
  slug: open-gitbook-organization-teams-api
- collection_type: open
  name: GitBook Change Request Content Organizations API
  slug: open-gitbook-organizations-api
- collection_type: open
  name: GitBook Change Request Content Search API
  slug: open-gitbook-search-api
- collection_type: open
  name: GitBook Change Request Content Site Spaces API
  slug: open-gitbook-site-spaces-api
- collection_type: open
  name: GitBook Change Request Content Space Content API
  slug: open-gitbook-space-content-api
- collection_type: open
  name: GitBook Change Request Content Space Users API
  slug: open-gitbook-space-users-api
- collection_type: open
  name: GitBook Change Request Content Spaces API
  slug: open-gitbook-spaces-api
- collection_type: open
  name: GitBook Change Request Content URLs API
  slug: open-gitbook-urls-api
- collection_type: open
  name: GitBook Change Request Content Users API
  slug: open-gitbook-users-api
common:
- group: other
  href: https://artifacts.apis.io/gitbook/capabilities/gitbook-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gitbook-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/gitbook/changelog/gitbook-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gitbook-changelog.yml
- group: auth
  href: https://artifacts.apis.io/gitbook/scopes/gitbook-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gitbook-scopes.yml
- group: commercial
  href: https://artifacts.apis.io/gitbook/finops/gitbook-finops.yml
  title: ''
  type: FinOps
  url: finops/gitbook-finops.yml
- group: operate
  href: https://artifacts.apis.io/gitbook/rate-limits/gitbook-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gitbook-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gitbook/plans/gitbook-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gitbook-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gitbook/rules/gitbook-rules.yml
  title: ''
  type: Spectral
  url: rules/gitbook-rules.yml
- group: design
  href: https://artifacts.apis.io/gitbook/rules/gitbook-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/gitbook-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/gitbook/rules/gitbook-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/gitbook-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/gitbook/vocabulary/gitbook-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gitbook-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gitbook/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gitbook/asyncapi/gitbook-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gitbook-webhooks.yml
- group: design
  href: https://artifacts.apis.io/gitbook/data-model/gitbook-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gitbook-data-model.yml
- group: build
  href: https://artifacts.apis.io/gitbook/cli/gitbook-cli.yml
  title: ''
  type: CLI
  url: cli/gitbook-cli.yml
- group: design
  href: https://artifacts.apis.io/gitbook/conventions/gitbook-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gitbook-conventions.yml
- group: design
  href: https://artifacts.apis.io/gitbook/errors/gitbook-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gitbook-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gitbook/conformance/gitbook-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gitbook-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gitbook/llms/gitbook-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gitbook-llms.txt
- group: agent
  href: https://artifacts.apis.io/gitbook/mcp/gitbook-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gitbook-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gitbook/well-known/gitbook-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gitbook-well-known.yml
- group: other
  href: https://artifacts.apis.io/gitbook/hosts/gitbook-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gitbook-hosts.yml
- group: other
  href: https://artifacts.apis.io/gitbook/vendors/gitbook-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gitbook-vendors.yml
- group: build
  href: https://artifacts.apis.io/gitbook/packages/gitbook-packages.yml
  title: ''
  type: SDKs
  url: packages/gitbook-packages.yml
- group: build
  href: https://artifacts.apis.io/gitbook/packages/gitbook-packages.yml
  title: ''
  type: Packages
  url: packages/gitbook-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.gitbook.com/integrations/webhook
- group: operate
  title: ''
  type: Support
  url: https://www.gitbook.com/solutions/help-center
- group: auth
  title: ''
  type: Security
  url: https://www.gitbook.com/industries/security
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gitbook.com/
- group: other
  href: https://artifacts.apis.io/gitbook/vendor-facets/gitbook-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/gitbook-vendor-facets.yml
- group: agent
  href: https://artifacts.apis.io/gitbook/agentic-access/gitbook-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gitbook-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gitbook/security/gitbook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gitbook-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gitbook/authentication/gitbook-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gitbook-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitbookio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gitbook
- group: company
  title: ''
  type: Website
  url: https://www.gitbook.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gitbook.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.gitbook.com/blog
- group: docs
  title: ''
  type: Guide
  url: https://gitbook.com/docs/guides
- group: start
  title: ''
  type: SignUp
  url: https://app.gitbook.com/join
- group: start
  title: ''
  type: GettingStarted
  url: https://gitbook.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://gitbook.com/docs/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://www.gitbookstatus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gitbook.com/docs/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gitbook.com/docs/policies/privacy-and-security/statement
- group: docs
  title: ''
  type: APIReference
  url: https://gitbook.com/docs/developers
- group: build
  title: ''
  type: SDK
  url: https://www.npmjs.com/package/@gitbook/api
created: '2025-01-08'
description: GitBook is a documentation and knowledge platform, positioned as "the knowledge layer for AI", that connects a company's docs, product and users, answers user questions with AI, and identifies gaps in its knowledge. Teams write and publish product and API documentation with docs-as-code support and AI insights built in.
finops:
- has_sources: true
  method: derived
  name: Gitbook Finops
  primary_unit: site/month
  service_category: ''
  slug: gitbook-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitbook.png
json_schemas:
- name: GitBook Change Request
  property_count: 9
  slug: change-request
- name: GitBook Collection
  property_count: 5
  slug: collection
- name: GitBook Docs Site
  property_count: 6
  slug: docs-site
- name: GitBook Organization
  property_count: 5
  slug: organization
- name: GitBook Page
  property_count: 7
  slug: page
- name: GitBook Space
  property_count: 8
  slug: space
- name: GitBook User
  property_count: 5
  slug: user
jsonld:
- class_count: 0
  name: Gitbook Context
  property_count: 7
  slug: gitbook-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.gitbook.com over HTTP.
  name: GitBook MCP Server
  slug: gitbook
modified: '2026-05-19'
name: GitBook
nav: Providers
network: true
overview: 'GitBook publishes 65 API contracts indexed on the [APIs.io](https://apis.io/) network, including Change Request Content API, Change Request Reviewers API, Change Requests API, and 62 more. Tagged areas include Content, Documentation, Experience, Integration, and Platform.


  The GitBook catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  GitBook''s developer surface includes changelog, CLI, support, documentation, authentication, pricing, engineering blog, and 39 more developer resources.'
plans:
- name: Gitbook Plans Pricing
  plan_count: 8
  slug: gitbook-plans-pricing
- name: Gitbook Price Estimates
  plan_count: 0
  slug: gitbook-price-estimates
random_paper: 7
rate_limits:
- limit_count: 5
  name: Gitbook Rate Limits
  slug: gitbook-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: GitBook — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: gitbook-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: GitBook — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gitbook-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: GitBook API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 2
    warn: 1
  slug: gitbook-rules
scopes:
- name: Gitbook Scopes
  scope_count: 29
  slug: gitbook-scopes
  summary_line: 29 scopes · authorizationCode
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 38
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 67.1
    contract_governance: 35.6
    contract_quality: 70.6
    developer_ergonomics: 51.8
    discoverability: 66.7
    operational_transparency: 35.5
  previous_composite: 70.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 76.5
      total: 85
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/gitbook/gitbook-2026-06-20T181833.png
security:
- kind: authentication
  name: Gitbook Authentication
  slug: gitbook-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gitbook Domain Security
  slug: gitbook-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: gitbook-collection-management
  slug: gitbook-collection-management
- name: gitbook-create-and-list-spaces
  slug: gitbook-create-and-list-spaces
- name: gitbook-manage-docs-sites
  slug: gitbook-manage-docs-sites
- name: gitbook-openapi-specs-workflow
  slug: gitbook-openapi-specs-workflow
slug: gitbook
tags:
- Content
- Documentation
- Experience
- Integration
- Platform
- SDK
- API Documentation
- Developer Portal
website: https://www.gitbook.com/
---
