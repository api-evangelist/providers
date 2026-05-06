---
aid: sourceforge
name: SourceForge
description: SourceForge is a web-based platform for hosting, managing, and distributing open source software projects. Built on the Apache Allura platform, SourceForge provides project management tools including wiki, issue tracking, discussion forums, blogs, file releases, code repositories (Git, SVN, Mercurial), and a REST API for programmatic access to all project resources.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Open Source
  - Developer Tools
  - Project Management
  - Code Hosting
  - Collaboration
created: '2026-03-16'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sourceforge/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sourceforge:sourceforge-allura-api
    name: SourceForge Allura API
    description: The SourceForge REST API built on Apache Allura provides programmatic access to project management, wiki pages, issue trackers, discussion forums, blogs, and administrative functions including webhooks. All endpoints follow the /rest/p/{project}/{tool} path pattern with OAuth 2.0 and OAuth 1.0 authentication.
    humanURL: https://sourceforge.net/p/forge/documentation/Allura%20API/
    baseURL: https://sourceforge.net
    tags:
      - Projects
      - Issues
      - Wiki
      - Discussions
      - Blogs
      - Webhooks
    properties:
      - type: Documentation
        url: https://sourceforge.net/p/forge/documentation/Allura%20API/
      - type: Reference
        url: https://sourceforge.net/api-docs/
      - type: Release API
        url: https://sourceforge.net/p/forge/documentation/Using%20the%20Release%20API/
      - type: Download Stats API
        url: https://sourceforge.net/p/forge/documentation/Download%20Stats%20API/
      - type: OAuth
        url: https://sourceforge.net/auth/oauth/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sourceforge/refs/heads/main/openapi/sourceforge-allura-openapi.yml
    contact:
      - FN: SourceForge Support
        url: https://sourceforge.net/p/forge/documentation/
        email: ''
common:
  - type: Portal
    url: https://sourceforge.net/p/forge/documentation/API/
  - type: Documentation
    url: https://sourceforge.net/p/forge/documentation/
  - type: Website
    url: https://sourceforge.net/
  - type: GitHub Org
    url: https://github.com/apache/allura
  - type: API Documentation
    url: https://sourceforge.net/api-docs/
  - type: OAuth Portal
    url: https://sourceforge.net/auth/oauth/
  - type: Webhooks Documentation
    url: https://forge-allura.apache.org/p/allura/wiki/Webhooks/
  - type: Support
    url: https://sourceforge.net/p/forge/site-support/
  - type: Blog
    url: https://sourceforge.net/blog/
  - type: Status
    url: https://sourceforge.net/p/forge/site-support/
  - type: Terms of Use
    url: https://sourceforge.net/p/forge/documentation/Terms%20of%20Use/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
