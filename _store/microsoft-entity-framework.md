---
aid: microsoft-entity-framework
name: Microsoft Entity Framework
description: Microsoft Entity Framework is an object-relational mapping (ORM) framework for .NET developers enabling database access using .NET objects. EF Core is the modern, cross-platform version supporting SQL Server, PostgreSQL, MySQL, SQLite, and Cosmos DB with LINQ queries, change tracking, migrations, and code-first modeling.
type: Index
image: https://docs.microsoft.com/en-us/ef/images/ef-logo.png
url: https://raw.githubusercontent.com/api-evangelist/microsoft-entity-framework/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - .NET
  - Data Access
  - Database
  - Entity Framework
  - ORM
apis:
  - aid: microsoft-entity-framework:ef-core
    name: Entity Framework Core
    description: A lightweight, extensible, open source and cross-platform ORM for .NET. Supports SQL Server, PostgreSQL, MySQL, SQLite, Cosmos DB, and in-memory databases.
    humanURL: https://learn.microsoft.com/en-us/ef/core/
    baseURL: https://www.nuget.org/packages/Microsoft.EntityFrameworkCore
    tags:
      - .NET Core
      - Cross-Platform
      - Database
      - ORM
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/ef/core/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/ef/core/get-started/overview/first-app
      - type: APIReference
        url: https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore
      - type: GitHubRepository
        url: https://github.com/dotnet/efcore
      - type: ReleaseNotes
        url: https://learn.microsoft.com/en-us/ef/core/what-is-new/
      - type: SDK
        url: https://www.nuget.org/packages/Microsoft.EntityFrameworkCore
        title: NuGet Package
  - aid: microsoft-entity-framework:ef6
    name: Entity Framework 6
    description: The mature and stable ORM for .NET Framework with Code First, Database First, and Model First workflows.
    humanURL: https://learn.microsoft.com/en-us/ef/ef6/
    baseURL: https://www.nuget.org/packages/EntityFramework
    tags:
      - .NET Framework
      - Database
      - Legacy
      - ORM
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/ef/ef6/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/ef/ef6/get-started
      - type: APIReference
        url: https://learn.microsoft.com/en-us/dotnet/api/system.data.entity
      - type: GitHubRepository
        url: https://github.com/dotnet/ef6
      - type: SDK
        url: https://www.nuget.org/packages/EntityFramework
        title: NuGet Package
common:
  - type: Portal
    url: https://learn.microsoft.com/en-us/ef/
  - type: Blog
    url: https://devblogs.microsoft.com/dotnet/tag/entity-framework/
  - type: GitHubOrganization
    url: https://github.com/dotnet
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/entity-framework-core
  - type: YouTube
    url: https://www.youtube.com/playlist?list=PLdo4fOcmZ0oX0ObHwBrJ0vJpZ7PiYMqeA
  - type: Support
    url: https://learn.microsoft.com/en-us/ef/core/get-started/overview/support
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Features
    data:
      - name: LINQ Queries
        description: Write database queries using Language Integrated Query (LINQ) with strongly-typed C# expressions.
      - name: Change Tracking
        description: Automatic tracking of entity changes for efficient database updates.
      - name: Migrations
        description: Database schema versioning with code-first migrations for evolving data models.
      - name: Code First Modeling
        description: Define database schemas using C# classes and data annotations or Fluent API.
      - name: Database Providers
        description: Plugin architecture supporting SQL Server, PostgreSQL, MySQL, SQLite, Cosmos DB, and more.
      - name: Lazy and Eager Loading
        description: Control related entity loading with lazy, eager, and explicit loading strategies.
      - name: Raw SQL Queries
        description: Execute raw SQL and stored procedures alongside LINQ queries.
      - name: Global Query Filters
        description: Apply automatic filtering to all queries for multi-tenancy and soft deletes.
      - name: Value Converters
        description: Custom type conversions between .NET types and database column types.
      - name: Compiled Queries
        description: Pre-compile LINQ queries for improved performance in hot paths.
  - type: UseCases
    data:
      - name: Web Application Data Access
        description: Data access layer for ASP.NET Core web applications and APIs.
      - name: Microservices Data Layer
        description: Database access for .NET microservices with per-service databases.
      - name: Database Migration Management
        description: Version-controlled schema evolution with automatic migration generation.
      - name: Multi-Database Applications
        description: Applications connecting to multiple database providers simultaneously.
      - name: Domain-Driven Design
        description: Implement DDD patterns with aggregate roots, value objects, and repositories.
      - name: Legacy Database Integration
        description: Map existing database schemas to modern .NET classes with Database First.
  - type: Solutions
    data:
      - name: Entity Framework Core
        description: Modern, cross-platform ORM for .NET 6+ applications.
      - name: Entity Framework 6
        description: Mature ORM for .NET Framework applications.
      - name: EF Core Tools
        description: CLI and Package Manager Console tools for migrations and scaffolding.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
