---
aid: flatfile
name: Flatfile
description: Flatfile is a data exchange platform that helps teams import, transform, validate, and collaborate on file-based data. The Flatfile API provides programmatic access to spaces, workbooks, sheets, records, files, documents, jobs, events, agents, environments, users, guests, and related primitives for building automated data onboarding and ingestion workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
tags:
  - Data Exchange
  - Data Ingestion
  - Data Onboarding
  - Data Validation
  - ETL
  - File Import
url: https://raw.githubusercontent.com/api-evangelist/flatfile/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: flatfile:flatfile-api
    name: Flatfile API
    description: 'The Flatfile API enables programmatic management of every primitive in the Flatfile platform: accounts, environments, spaces, workbooks, sheets, records, snapshots, commits, versions, files, documents, jobs, events, agents, agent exports, actions, mappings, runbooks, data clips, canvas areas, views, flags, secrets, roles, users, guests, entitlements, apps, auth, data retention policies, and assistant operations.'
    humanURL: https://reference.flatfile.com/
    baseURL: https://api.x.flatfile.com/v1
    tags:
      - Accounts
      - Agents
      - Apps
      - Auth
      - Documents
      - Environments
      - Events
      - Files
      - Guests
      - Jobs
      - Mapping
      - Records
      - Roles
      - Secrets
      - Sheets
      - Snapshots
      - Spaces
      - Users
      - Views
      - Workbooks
    properties:
      - type: Documentation
        url: https://flatfile.com/docs/
      - type: APIReference
        url: https://reference.flatfile.com/
      - type: OpenAPI
        url: openapi/flatfile-api-openapi.yml
      - type: GettingStarted
        url: https://flatfile.com/docs/quickstart
common:
  - type: Website
    url: https://flatfile.com/
  - type: Documentation
    url: https://flatfile.com/docs/
  - type: APIReference
    url: https://reference.flatfile.com/
  - type: OpenAPI
    url: https://reference.flatfile.com/openapi.json
  - type: GettingStarted
    url: https://flatfile.com/docs/quickstart
  - type: SignUp
    url: https://flatfile.com/account/sign-up/
  - type: Pricing
    url: https://flatfile.com/pricing/
  - type: Blog
    url: https://flatfile.com/blog/
  - type: SDKs
    url: https://flatfile.com/docs/sdks
  - type: GitHubOrganization
    url: https://github.com/FlatFilers
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
