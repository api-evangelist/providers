---
aid: reddit
name: Reddit
description: Reddit is a social news aggregation, discussion, and community platform where users submit, vote, and comment on content organized into topic-based communities called subreddits. Reddit provides developer APIs for accessing platform data, managing communities, running advertising campaigns, and embedding content. The Reddit Data API provides access to posts, comments, subreddits, user profiles, and moderation tools via OAuth 2.0. The Reddit Ads API enables programmatic management of advertising campaigns, audiences, and conversion tracking. All API access requires OAuth 2.0 authentication via the oauth.reddit.com server at 60 requests per minute.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Advertising
  - Communities
  - Content
  - Social Media
  - Social News
url: https://raw.githubusercontent.com/api-evangelist/reddit/refs/heads/main/apis.yml
created: '2026-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: reddit:data-api
    name: Reddit Data API
    description: The Reddit Data API provides programmatic access to Reddit content including subreddits, posts, comments, user profiles, and voting data. Developers can use the API to read and submit content, manage subreddits, search across the platform, interact with Reddit communities, handle private messages, and manage flair. All requests require OAuth 2.0 authentication via oauth.reddit.com with rate limits of 60 requests per minute for authenticated clients. A Data API Terms agreement is required for high-volume access.
    humanURL: https://www.reddit.com/dev/api
    baseURL: https://oauth.reddit.com
    tags:
      - Comments
      - Communities
      - Content
      - Posts
      - Social Media
      - Subreddits
    properties:
      - type: Documentation
        url: https://www.reddit.com/dev/api
      - type: Authentication
        url: https://github.com/reddit-archive/reddit/wiki/OAuth2
      - type: Terms of Service
        url: https://www.redditinc.com/policies/data-api-terms
      - type: OpenAPI
        url: openapi/reddit-data-api-openapi.yml
  - aid: reddit:ads-api
    name: Reddit Ads API
    description: The Reddit Ads API allows advertisers and their marketing partners to programmatically create, edit, manage, and report on advertising campaigns on the Reddit platform. It provides endpoints for managing ad accounts, campaigns, ad groups, ads, creatives, targeting configurations, custom audiences (email lists, mobile IDs, pixel-based), conversion pixels, and performance reporting. Authentication uses OAuth 2.0 with a rate limit of one request per second per advertiser account.
    humanURL: https://ads-api.reddit.com/docs/
    baseURL: https://ads-api.reddit.com/api/v3
    tags:
      - Advertising
      - Campaigns
      - Marketing
      - Social Media
      - Targeting
    properties:
      - type: Documentation
        url: https://ads-api.reddit.com/docs/
      - type: Terms of Service
        url: https://business.reddithelp.com/s/article/Reddit-Ads-API-Terms
      - type: OpenAPI
        url: openapi/reddit-ads-api-openapi.yml
  - aid: reddit:embeds
    name: Reddit Embeds (oEmbed)
    description: Reddit Embeds allows developers and content creators to embed Reddit posts and comments directly into external websites and applications. The service provides oEmbed endpoints that return embed codes and metadata for rendering Reddit content in a visually consistent format outside of the Reddit platform. It follows the oEmbed specification for content discovery and embedding, returning HTML embed code for any Reddit post or comment URL.
    humanURL: https://oembed.com/
    baseURL: https://www.reddit.com
    tags:
      - Content
      - Embedding
      - oEmbed
      - Social Media
    properties:
      - type: Documentation
        url: https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data
      - type: OpenAPI
        url: openapi/reddit-embeds-openapi.yml
  - aid: reddit:oauth
    name: Reddit OAuth 2.0 Authorization
    description: Reddit's OAuth 2.0 authorization system provides authentication for all Reddit API access. Developers register applications at reddit.com/prefs/apps to obtain client credentials. Supported grant types include authorization_code (for user-delegated access), client_credentials (for app-only access), and implicit (for installed apps). Access tokens are obtained from https://www.reddit.com/api/v1/access_token and must be refreshed using refresh tokens. All scopes and permissions are listed at https://www.reddit.com/api/v1/scopes.
    humanURL: https://github.com/reddit-archive/reddit/wiki/OAuth2
    baseURL: https://www.reddit.com/api/v1
    tags:
      - Authentication
      - Authorization
      - OAuth 2.0
      - Security
    properties:
      - type: Documentation
        url: https://github.com/reddit-archive/reddit/wiki/OAuth2
      - type: Scopes
        url: https://www.reddit.com/api/v1/scopes
      - type: App Registration
        url: https://www.reddit.com/prefs/apps
common:
  - type: Website
    url: https://www.reddit.com
  - type: Developer Portal
    url: https://www.reddit.com/dev/api
  - type: Documentation
    url: https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki
  - type: GitHub Organization
    url: https://github.com/reddit-archive
  - type: Blog
    url: https://www.redditinc.com/blog
  - type: Privacy Policy
    url: https://www.reddit.com/policies/privacy-policy
  - type: Terms of Service
    url: https://www.redditinc.com/policies/user-agreement
  - type: Status
    url: https://www.redditstatus.com/
  - type: Support
    url: https://support.reddithelp.com/hc/en-us
  - type: Sign Up
    url: https://www.reddit.com/register
  - type: OpenAPI
    url: openapi/reddit-data-api-openapi.yml
  - type: OpenAPI
    url: openapi/reddit-ads-api-openapi.yml
  - type: OpenAPI
    url: openapi/reddit-embeds-openapi.yml
  - type: JSONSchema
    url: json-schema/reddit-post-schema.json
  - type: JSONSchema
    url: json-schema/reddit-comment-schema.json
  - type: JSONSchema
    url: json-schema/reddit-subreddit-schema.json
  - type: JSONLDContext
    url: json-ld/reddit-context.jsonld
  - type: JSONStructure
    url: json-structure/reddit-post-structure.json
  - type: SpectralRuleset
    url: rules/reddit-rules.yml
  - type: NaftikoCapability
    url: capabilities/community-engagement.yaml
  - type: NaftikoCapability
    url: capabilities/advertising.yaml
  - type: Vocabulary
    url: vocabulary/reddit-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
