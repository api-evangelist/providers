---
aid: convention-over-configuration
url: https://raw.githubusercontent.com/api-evangelist/convention-over-configuration/refs/heads/main/apis.yml
name: Convention Over Configuration
x-type: topic
description: Convention over Configuration (CoC) is a software design principle that prefers sensible defaults and standard patterns over explicit, repetitive configuration. Frameworks that adopt CoC reduce the number of decisions a developer must make to start a new project while still allowing overrides for non-standard cases. CoC was popularized by Ruby on Rails but predates Rails, drawing on UI principles like the principle of least astonishment and conventions in JavaBeans, Maven, and other Java ecosystems. The principle continues to shape modern frameworks such as Spring Boot, Next.js, Astro, Phoenix, Ember, Hugo, and Remix.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Conventions
  - Design Principle
  - Frameworks
  - Software Design
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: convention-over-configuration:rails
    name: Ruby on Rails
    description: Ruby on Rails is the framework that popularized convention over configuration. By default, an ActiveRecord model named Sale maps to a sales table, controllers map to RESTful resources, and the directory layout under app/ implies wiring without explicit configuration files.
    humanURL: https://rubyonrails.org/
    baseURL: https://rubyonrails.org
    tags:
      - Active Record
      - Rails
      - Ruby
    properties:
      - type: Documentation
        url: https://rubyonrails.org/doctrine
      - type: Reference
        url: https://guides.rubyonrails.org/getting_started.html
    x-features:
      - Pluralized table inference for ActiveRecord models
      - RESTful controller routing inferred from resource names
      - Generators for resources, migrations, and tests
      - Pattern of opinionated defaults with override hooks
    x-useCases:
      - Bootstrapping production web applications quickly
      - Establishing consistent codebases across teams
  - aid: convention-over-configuration:spring-boot
    name: Spring Boot
    description: Spring Boot is the convention-over-configuration evolution of the Spring Framework. Auto-configuration detects classpath dependencies and wires beans automatically, starter dependencies bundle common stacks, and standard application.yml properties shape behavior with sensible defaults.
    humanURL: https://spring.io/projects/spring-boot
    baseURL: https://spring.io
    tags:
      - Auto-Configuration
      - Java
      - Spring
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-boot/index.html
      - type: Reference
        url: https://spring.io/projects/spring-boot
    x-features:
      - Auto-configuration based on classpath presence
      - Spring Boot starters for common stacks
      - Externalized configuration via application.yml/properties
      - Embedded servers and standalone JAR packaging
    x-useCases:
      - Bootstrapping enterprise Java microservices
      - Reducing XML and Java configuration boilerplate
  - aid: convention-over-configuration:maven
    name: Apache Maven
    description: Apache Maven introduced a strict project layout (src/main/java, src/test/java, target/) and a convention-driven build lifecycle. A pom.xml that declares dependencies and a parent POM is enough for most Java projects to compile, test, package, and deploy.
    humanURL: https://maven.apache.org/
    baseURL: https://maven.apache.org
    tags:
      - Build
      - Java
      - Maven
    properties:
      - type: Documentation
        url: https://maven.apache.org/guides/introduction/introduction-to-the-pom.html
      - type: Reference
        url: https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html
    x-features:
      - Standard directory layout for Java projects
      - Convention-driven phases (compile, test, package, install, deploy)
      - Plugin architecture for custom phases
      - Inheritance via parent POMs
    x-useCases:
      - Standardizing build tooling across Java projects
      - Hosting and consuming artifacts from Maven Central
  - aid: convention-over-configuration:next-js
    name: Next.js
    description: Next.js exemplifies convention over configuration in modern web frameworks. The pages and app directory conventions auto-generate routes, file-based layouts, error boundaries, loading UI, and API routes without explicit router configuration.
    humanURL: https://nextjs.org/
    baseURL: https://nextjs.org
    tags:
      - Next.js
      - React
      - Web
    properties:
      - type: Documentation
        url: https://nextjs.org/docs
      - type: Reference
        url: https://nextjs.org/docs/app/building-your-application/routing
    x-features:
      - File-system-based routing
      - app/ conventions for layouts, loading, and error UIs
      - Auto-generated API routes from app/api/* paths
      - Conventions for static and dynamic rendering
    x-useCases:
      - Building React applications with minimal routing config
      - Standardizing front-end architecture across teams
  - aid: convention-over-configuration:hugo
    name: Hugo Static Site Generator
    description: Hugo defines content, layouts, archetypes, and partials by directory convention. A content/posts directory yields a section with a list page and per-post pages without explicit routing configuration.
    humanURL: https://gohugo.io/
    baseURL: https://gohugo.io
    tags:
      - Go
      - Hugo
      - Static Sites
    properties:
      - type: Documentation
        url: https://gohugo.io/documentation/
      - type: Reference
        url: https://gohugo.io/getting-started/directory-structure/
    x-features:
      - Section-based content directory layout
      - Layout lookup order with sensible fallbacks
      - Archetypes for templating new content files
      - Configuration-light defaults with TOML/YAML overrides
    x-useCases:
      - Building documentation sites with little setup
      - Producing fast static sites with default conventions
common:
  - type: Reference
    url: https://en.wikipedia.org/wiki/Convention_over_configuration
  - type: Reference
    url: https://rubyonrails.org/doctrine
  - type: Reference
    url: https://docs.spring.io/spring-boot/index.html
  - type: Reference
    url: https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html
  - type: Reference
    url: https://nextjs.org/docs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
