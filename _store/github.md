---
aid: github
url: https://raw.githubusercontent.com/api-search/code/main/_apis/github/apis.md
apis:
  - aid: github:github-app-api
    name: GitHub App API
    tags:
      - Applications
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/apps?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-app-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-app-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/apps
        type: Documentation
    description: |-
      Use the REST API to retrieve information about GitHub Apps and GitHub App
      installations.
  - aid: github:github-auth-api
    name: GitHub Authorization API
    tags:
      - Authorization
      - Authentication
    baseURL: https://api.github.com
    humanURL: >-
      https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
    properties:
      - url: properties/github-auth-api-openapi.yml
        type: OpenAPI
      - url: >-

          https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
        type: Documentation
    description: |-

      You can authenticate to the REST API to access more endpoints and have a
      higher rate limit.
  - aid: github:github-code-of-conduct-api
    name: GitHub Code of Conduct API
    tags:
      - Code of Conduct
    baseURL: https://api.github.com
    humanURL: >-
      https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct?apiVersion=2022-11-28
    properties:
      - url: properties/github-code-of-conduct-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/codes-of-conduct/codes-of-conduct
        type: Documentation
    description: Use the REST API to get information about codes of conduct.
  - aid: github:github-emojis-api
    name: GitHub Emojis API
    tags:
      - Emojis
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/emojis?apiVersion=2022-11-28
    properties:
      - url: openapi/github-emojis-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/emojis
        type: Documentation
    description: |-

      Use the REST API to list and view all the available emojis to use on
      GitHub.
  - aid: github:github-events-api
    name: GitHub Events API
    tags:
      - Events
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28
    properties:
      - url: properties/github-events-api-openapi.yml
        type: OpenAPI
    description: Use the REST API to interact with GitHub events.
  - aid: github:github-feeds-api
    name: GitHub Feeds API
    tags:
      - Feeds
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/activity/feeds?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-feeds-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-feeds-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the REST API to interact with GitHub feeds. Lists the feeds available
      to the authenticated user. The response provides a URL for each feed. You
      can then get a specific feed by sending a request to one of the feed URLs.
  - aid: github:github-gists-api
    name: GitHub Gists API
    tags:
      - Gists
      - Code
      - Artifacts
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/gists?apiVersion=2022-11-28
    properties:
      - url: properties/github-gists-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Gists REST API provides endpoints for managing public gists on
      GitHub. It allows developers to programmatically list, create, update, and
      delete gistswhich are simple ways to share code snippets, notes, and other
      content with others. Through this API, you can perform all the essential
      operations needed to view and modify gists without using GitHub's web
      interface, making it easy to integrate gist management into your
      applications or workflows.
  - aid: github:github-gitignore-templates-api
    name: GitHub Gitignore Templates API
    tags:
      - Templates
      - Gitignore
    baseURL: https://api.github.com
    humanURL: https://docs.github.com/en/rest/gitignore?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-gitignore-templates-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-gitignore-templates-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the REST API to get .gitignore templates that can be used to ignore
      files and directories.
  - aid: github:github-installation-api
    name: GitHub Installation API
    tags:
      - Installations
    baseURL: https://api.github.com/
    properties:
      - url: properties/github-installation-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the REST API to get information about GitHub App installations and
      perform actions within those installations.
  - aid: github:github-issues-api
    name: GitHub Issues API
    tags:
      - Issues
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/issues?apiVersion=2022-11-28
    properties:
      - url: properties/github-issues-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the REST API to view and manage issues, including issue assignees,
      comments, labels, and milestones.
  - aid: github:github-licenses-api
    name: GitHub Licenses API
    tags:
      - Licenses
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/licenses?apiVersion=2022-11-28
    properties:
      - url: properties/github-licenses-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the REST API to retrieve popular open source licenses and information
      about a particular project's license file.
  - aid: github:github-manage-api
    name: GitHub Enterprise Management API
    tags:
      - Management
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-manage-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-manage-api-openapi.yml
        type: OpenAPI
    description: >-
      You can manage your GitHub Enterprise Server instance using the Manage
      GitHub Enterprise Server API. For example, you can retrieve information
      about the version of the GitHub Enterprise Server software running on the
      instance, or on instances with multiple nodes, view the status of
      replication.
  - aid: github:github-markdown-api
    name: GitHub Markdown API
    tags:
      - Markdown
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/markdown?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-markdown-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-markdown-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/markdown
        type: Documentation
    description: |-

      Use the REST API to render a Markdown document as an HTML page or as raw
      text.
  - aid: github:github-meta-api
    name: GitHub Meta API
    tags:
      - Metadata
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/meta?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-meta-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-meta-api-openapi.yml
        type: OpenAPI
      - url: https://docs.github.com/en/rest/meta
        type: Documentation
    description: |-

      Use the REST API to get meta information about GitHub, including the IP
      addresses of GitHub services.
  - aid: github:github-networks-api
    name: GitHub Networks API
    tags:
      - Networks
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-networks-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-networks-api-openapi.yml
        type: OpenAPI
    description: Needs description.
  - aid: github:github-notifications-api
    name: GitHub Notifications API
    tags:
      - Notifications
    baseURL: https://api.github.com/
    humanURL: >-

      https://docs.github.com/en/rest/activity/notifications?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-notifications-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-notifications-api-openapi.yml
        type: OpenAPI
    description: >-
      This GitHub REST API allows you to programmatically manage your GitHub
      notifications, which include updates on issues, pull requests, and
      commits. The API requires authentication via a personal access token
      (classic) and needs either the notifications or repo scope to function. 
  - aid: github:github-octocat-api
    name: GitHub Octocat API
    tags:
      - Octocat
    baseURL: https://api.github.com/
    humanURL: https://github.com/octokit/octokit.js
    overlays:
      - url: overlays/github-octocat-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-octocat-api-openapi.yml
        type: OpenAPI
    description: >-
      Offers a basic endpoint to fetch the Octocat as ASCII art and provides a
      default Octocat image URL. 
  - aid: github:github-org-api
    name: GitHub Organization API
    tags:
      - Organizations
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/orgs?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-org-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-org-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Organization APIs allow you to programmatically manage and
      interact with GitHub organizations, which are shared accounts where groups
      of people can collaborate across multiple projects simultaneously. Through
      these REST API endpoints, you can perform administrative tasks such as
      creating and managing organizations, handling organization memberships and
      team structures, configuring organization settings and permissions,
      managing organization-wide resources like webhooks and secrets, and
      accessing organization-level analytics and audit logs.
  - aid: github:github-projects-api
    name: GitHub Projects API
    tags:
      - Projects
    baseURL: https://api.github.com/
    overlays:
      - url: overlays/github-projects-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-projects-api-openapi.yml
        type: OpenAPI
    description: >-
      The GitHub Projects API enables developers to programmatically create and
      manage GitHub Projects, which are flexible tools for planning and tracking
      work using customizable boards, tables, and roadmaps. Through these REST
      API endpoints, you can create projects at the repository, organization, or
      user level, add and organize items like issues and pull requests, manage
      project fields and views, update item statuses and metadata, and automate
      project workflows. This API is particularly useful for integrating project
      management functionality into custom applications, automating project
      updates based on repository events, building dashboards and reporting
      tools, or synchronizing GitHub project data with external project
      management systems.
  - aid: github:github-rate-limit-api
    name: GitHub Rate Limit API
    tags:
      - Rate Limits
    baseURL: https://api.github.com/
    humanURL: >-

      https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-rate-limit-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-rate-limit-openapi.yml
        type: OpenAPI
    description: |-

      Learn about REST API rate limits, how to avoid exceeding them, and what to
      do if you do exceed them.
  - aid: github:github-repos-api
    name: GitHub Repos API
    tags:
      - Repos
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/repos?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-repos-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-repos-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the REST API to create, manage and control the workflow of public and
      private GitHub repositories.
  - aid: github:github-scim-api
    name: GitHub SCIM API
    tags:
      - SCIM
    baseURL: https://api.github.com/
    humanURL: >-

      https://docs.github.com/en/enterprise-cloud@latest/rest/scim?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-scim-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-scim-openapi.yml
        type: OpenAPI
    description: |-

      Use the REST API to control and manage your GitHub organization members'
      access with SCIM.
  - aid: github:github-search-api
    name: GitHub Search API
    tags:
      - Search
      - Discovery
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-search-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/github-search-api-openapi.yml
        type: OpenAPI
    description: Use the REST API to search for specific items on GitHub.
  - aid: github:github-setup-api
    name: GitHub Setup API
    tags:
      - Setup
    baseURL: https://api.github.com/
    humanURL: >-
      https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
    overlays:
      - url: overlays/github-setup-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-setup-openapi.yml
        type: OpenAPI
    description: Use the REST API to create and manage teams in your GitHub organization.
  - aid: github:github-teams-api
    name: GitHub Teams API
    tags:
      - Teams
    baseURL: https://api.github.com/
    overlays:
      - url: overlays/github-teams-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-teams-openapi.yml
        type: OpenAPI
    description: Needs description.
  - aid: github:github-zen-api
    name: GitHub Zen API
    tags:
      - Zen
    overlays:
      - url: overlays/github-zen-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/github-zen-openapi.yml
        type: OpenAPI
    description: Needs description.
  - aid: github:github-user-api
    name: GitHub User API
    tags:
      - Users
    baseURL: https://api.github.com/
    humanURL: https://docs.github.com/en/rest/users?apiVersion=2022-11-28
    properties:
      - url: properties/github-users-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the REST API to get public and private information about authenticated
      users.
name: GitHub
tags:
  - Code
  - Source Control
  - Software Development
  - Platform
  - Pipelines
  - T1
type: Contract
access: 3rd-Party
common:
  - url: https://github.com/pricing
    data:
      - id: free
        name: Free
        addOns:
          - name: GitHub Copilot Access
            description: >-
              With GitHub Copilot, get suggestions for whole lines or entire
              functionsright inside your editor.
          - name: GitHub Codespaces Access
            description: >-
              With GitHub Codespaces, get an instant dev environment in the
              cloud, so you can code anywhere on any device.
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Usage based pricing.
          - geo: US
            unit: 1
            label: CI/CD Minutes
            limit: 2000
            price: Free
            metric: ci-cd-minute
            timeFrame: minutes
            description: CI/CD minutes usage.
          - geo: US
            unit: 1
            label: Package Storage
            limit: 500
            price: Free
            metric: mb
            description: The amount of package storage.
        elements:
          - name: Unlimited Public Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Unlimited Private Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Dependabot Security Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Dependabot Version Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Issues
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Projects
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Community Support
            description: >-
              Get help with most of your GitHub questions and issues in our
              Community Forum.
        description: The basics for individuals and organizations
      - id: team
        name: Team
        addOns:
          - name: GitHub Secret Protection
            description: >-
              Ensure your secrets stay secure. Mitigate risk associated with
              exposed secrets in your repositories, while preventing new leaks
              before they happen with push protection.
          - name: GitHub Code Security
            description: >-
              Find and fix vulnerabilities in your code before they reach
              production. Prioritize your Dependabot alerts with automated
              triage rules.
        entries:
          - geo: US
            unit: 1
            label: User
            price: '4.00'
            metric: user
            timeFrame: month
            description: Usage based pricing.
          - geo: US
            unit: 1
            label: CI/CD Minutes
            limit: 2000
            price: Free
            metric: ci-cd-minute
            timeFrame: minutes
            description: CI/CD minutes usage.
          - geo: US
            unit: 1
            label: Package Storage
            limit: 500
            price: Free
            metric: mb
            description: The amount of package storage.
        elements:
          - name: Unlimited Public Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Unlimited Private Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Dependabot Security Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Dependabot Version Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Issues
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Projects
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Community Support
            description: >-
              Get help with most of your GitHub questions and issues in our
              Community Forum.
          - name: Access to GitHub Codespaces
            description: >-
              Blazing fast cloud developer environments with flexible compute
              and pre-configured containers, developers can code, collaborate,
              and debug from any browser. Pay only for what you use with compute
              fees starting at $0.18/hr and storage fees at $0.07/GB per month.
          - name: Protected Branches
            description: >-
              Enforce restrictions on how code branches are merged, including
              requiring reviews by selected collaborators, or allowing only
              specific contributors to work on a particular branch.
          - name: Multiple Reviewers in Pull Requests
            description: Assign multiple users or a team to review a pull request.
          - name: Draft Pull Requests
            description: >-
              Easily discuss and collaborate on pull requests before submitting
              to formal review.
          - name: Code Owners
            description: >-
              Automatically request reviewsor require approvalby selected
              contributors when changes are made to sections of code that they
              own.
          - name: Required Reviewers
            description: >-
              Ensure that pull requests have a specific number of approving
              reviews before collaborators can make changes to a protected
              branch.
          - name: Pages & Wikis
            description: >-
              Host documentation and simple websites for your project in a wiki
              format that contributors can easily edit either on the web or
              command line.
          - name: Environmental Deployment Branches and Secrets
            description: >-
              A job cannot access secrets that are defined in an environment
              unless it is running on the specified branch.
          - name: Web Based Support
            description: >-
              GitHub Support can help you troubleshoot issues you run into while
              using GitHub.
        description: Advanced collaboration for individuals and organizations.
      - id: enterprise
        name: Enterprise
        addOns:
          - name: Premium Support
            description: >-
              With Premium, get a 30-minute SLA on Urgent tickets and 24/7 web
              and phone support via callback request. With Premium Plus, get
              everything in Premium, assigned Customer Reliability Engineer and
              more.
        entries:
          - geo: US
            unit: 1
            label: User
            price: '21.00'
            metric: user
            timeFrame: month
            description: Usage based pricing.
          - geo: US
            unit: 1
            label: CI/CD Minutes
            limit: 50000
            price: Free
            metric: ci-cd-minute
            timeFrame: minutes
            description: CI/CD minutes usage.
          - geo: US
            unit: 1
            label: Package Storage
            limit: 50
            price: Free
            metric: gb
            description: The amount of package storage.
        elements:
          - name: Unlimited Public Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Unlimited Private Repositories
            description: >-
              Host open source projects in public GitHub repositories,
              accessible via web or command line. Public repositories are
              accessible to anyone at GitHub.com.
          - name: Dependabot Security Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Dependabot Version Updates
            description: >-
              Keep projects secure by automatically opening pull requests to
              update vulnerable dependencies and keep them up to date.
          - name: Issues
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Projects
            description: >-
              Give your developers flexible features for project management that
              adapts to any team, project, and workflow  all alongside your
              code.
          - name: Community Support
            description: >-
              Get help with most of your GitHub questions and issues in our
              Community Forum.
          - name: Access to GitHub Codespaces
            description: >-
              Blazing fast cloud developer environments with flexible compute
              and pre-configured containers, developers can code, collaborate,
              and debug from any browser. Pay only for what you use with compute
              fees starting at $0.18/hr and storage fees at $0.07/GB per month.
          - name: Protected Branches
            description: >-
              Enforce restrictions on how code branches are merged, including
              requiring reviews by selected collaborators, or allowing only
              specific contributors to work on a particular branch.
          - name: Multiple Reviewers in Pull Requests
            description: Assign multiple users or a team to review a pull request.
          - name: Draft Pull Requests
            description: >-
              Easily discuss and collaborate on pull requests before submitting
              to formal review.
          - name: Code Owners
            description: >-
              Automatically request reviewsor require approvalby selected
              contributors when changes are made to sections of code that they
              own.
          - name: Required Reviewers
            description: >-
              Ensure that pull requests have a specific number of approving
              reviews before collaborators can make changes to a protected
              branch.
          - name: Pages & Wikis
            description: >-
              Host documentation and simple websites for your project in a wiki
              format that contributors can easily edit either on the web or
              command line.
          - name: Environmental Deployment Branches and Secrets
            description: >-
              A job cannot access secrets that are defined in an environment
              unless it is running on the specified branch.
          - name: Data Residency
            description: >-
              GitHub Enterprise Cloud offers a multi-tenant enterprise SaaS
              solution on Microsoft Azure, allowing you to choose a regional
              cloud deployment for data residency, so your in-scope data is
              stored at rest in a designated location. Start a free 30 day trial
              today or contact our sales team for more information.
          - name: Managed Users
            description: >-
              Own and control the user accounts of your enterprise members
              through your identity provider (IdP).
          - name: User Provisioning Through SCIM
            description: >-
              Automatically invite members to join your organization when you
              grant access on your IdP. If you remove a member's access to your
              GitHub organization on your SAML IdP, the member will be
              automatically removed from the GitHub organization.
          - name: Centrall Manage Multiple Organizations
            description: >-
              GitHub Enterprise Cloud includes the option to create an
              enterprise account, which enables collaboration between multiple
              organizations, gives administrators a single point of visibility
              and management and brings license cost savings for identical users
              in multiple organizations
          - name: Environment Protection Rules
            description: >-
              When a workflow job references an environment, the job won't start
              until all of the environment's protection rules pass.
          - name: Repository Rules
            description: >-
              Enforce branch and tag restrictions across your organization,
              ensuring branch and tag protection across your repositories.
              Evaluate rules to assess impact before enforcement.
          - name: Audit Log API
            description: >-
              As a GitHub Enterprise Cloud organization administrator, you can
              now access log events using our GraphQL API and monitor the
              activity in your organization.
          - name: Annual SOC Reports
            description: >-
              GitHub offers AICPA System and Organization Controls (SOC) 1 Type
              2 and SOC 2 Type 2 reports with IAASB International Standards on
              Assurance Engagements, ISAE 3000, and ISAE 3402.
          - name: FedRAMP
            description: >-
              Government users can host projects on GitHub Enterprise Cloud with
              the confidence that our platform meets the low impact
              software-as-a-service (SaaS) baseline of security standards set by
              our U.S. federal government partners.
          - name: SAML Single Sign-On
            description: >-
              Use an identity provider to manage the identities of GitHub users
              and applications.
          - name: Advanced Auditing
            description: >-
              Quickly review the actions performed by members of your
              organization. Keep copies of audit log data to ensure secure IP
              and maintain compliance for your organization.
          - name: GitHub Connect
            description: >-
              Share features and workflows between your GitHub Enterprise Server
              instance and GitHub Enterprise Cloud.
        description: Security, compliance, and flexible deployment
    name: Plans
    type: Plans
  - url: https://github.com/github/roadmap
    name: Road Map
    type: RoadMap
  - url: https://github.com/about
    name: About GitHub
    type: About
  - url: >-
      https://docs.github.com/en/get-started/exploring-integrations/about-building-integrations
    name: About building integrations - GitHub Docs
    type: Documentation
  - url: https://www.githubstatus.com/
    name: Status
    type: Status
  - url: https://cli.github.com/
    name: GitHub CLI | Take GitHub to the command line
    type: CLI
  - url: https://github.com/github
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://support.github.com/
    name: GitHub Support
    type: Support
  - url: https://github.com/partners/
    name: GitHub  Where software is built
    type: Partners
  - url: https://github.com/partners/
    name: GitHub  Where software is built
    type: Partners
  - url: >-
      https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
    name: GitHub Terms of Service - GitHub Docs
    type: TermsOfService
  - url: >-
      https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
    name: GitHub General Privacy Statement - GitHub Docs
    type: PrivacyPolicy
  - url: >-
      https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
    name: GitHub General Privacy Statement - GitHub Docs
    type: PrivacyPolicy
  - url: >-
      https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
    name: Rate limits for the REST API - GitHub Docs
    type: RateLimits
  - url: >-
      https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28
    name: Using pagination in the REST API - GitHub Docs
    type: Pagination
  - url: >-
      https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
    name: Authenticating to the REST API - GitHub Docs
    type: Authentication
  - url: >-
      https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
    name: Getting started with the REST API - GitHub Docs
    type: GettingStarted
created: 2024/04/14
modified: '2025-12-23'
position: Consuming
description: >-
  GitHub is a cloud-based platform for software development and version control,
  built on Git. It enables developers to store, manage, and collaborate on code.
  In addition to Gits distributed version control, GitHub offers access control,
  bug tracking, feature requests, task management, continuous integration, and
  wikis for projects. Headquartered in California, it has operated as a
  subsidiary of Microsoft since 2018.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'
---