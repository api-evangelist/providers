---
aid: thymeleaf
name: Thymeleaf
description: Thymeleaf is a modern server-side Java template engine for both web and standalone environments, capable of processing HTML, XML, JavaScript, CSS, and plain text. Its primary goal is to bring elegant natural templates to development workflows — HTML pages that can be correctly displayed in browsers as static prototypes while also working as dynamic server-side templates. With over 3,000 GitHub stars, Thymeleaf 3.1 offers deep Spring Framework integration via the Spring Standard Dialect using Spring EL, extensive tool support for Eclipse and IntelliJ IDEA, and an extensible dialect system. It is widely used in Spring Boot web applications as the standard server-side rendering solution.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - HTML
  - Java
  - Open Source
  - Server Side Rendering
  - Spring
  - Spring Boot
  - Template Engine
  - Thymeleaf
  - Web Development
url: https://raw.githubusercontent.com/api-evangelist/thymeleaf/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: thymeleaf:thymeleaf-core
    name: Thymeleaf Core
    description: 'The core Thymeleaf template engine library providing HTML, XML, TEXT, JavaScript, and CSS template mode processing. Includes the Standard Dialect with th:text, th:each, th:if, th:unless, th:switch, th:href, th:src, th:action, th:object, th:field expressions and the Standard Expression Syntax using ${...} variable expressions, *{...} selection expressions, #{...} message expressions, @{...} URL expressions, and ~{...} fragment expressions.'
    humanURL: https://www.thymeleaf.org/
    baseURL: https://www.thymeleaf.org/
    tags:
      - HTML
      - Java
      - Open Source
      - Template Engine
      - Thymeleaf
    properties:
      - type: Documentation
        url: https://www.thymeleaf.org/doc/tutorials/3.1/usingthymeleaf.html
      - type: Getting Started
        url: https://www.thymeleaf.org/doc/tutorials/3.1/usingthymeleaf.html#a-first-taste-of-thymeleaf
      - type: GitHub
        url: https://github.com/thymeleaf/thymeleaf
      - type: Maven
        url: https://mvnrepository.com/artifact/org.thymeleaf/thymeleaf
      - type: Changelog
        url: https://github.com/thymeleaf/thymeleaf/releases
    version: 3.1.5.RELEASE
  - aid: thymeleaf:thymeleaf-spring-integration
    name: Thymeleaf Spring Integration
    description: The Thymeleaf Spring integration module (thymeleaf-spring6) providing deep integration with Spring Framework including the SpringStandardDialect using Spring EL, SpringTemplateEngine auto-configuration, Spring MVC view resolver integration, Spring Security dialect, form binding support, internationalization with Spring MessageSource, and Spring Boot starter.
    humanURL: https://www.thymeleaf.org/doc/tutorials/3.1/thymeleafspring.html
    baseURL: https://www.thymeleaf.org/
    tags:
      - Java
      - Spring
      - Spring Boot
      - Spring MVC
      - Template Engine
    properties:
      - type: Documentation
        url: https://www.thymeleaf.org/doc/tutorials/3.1/thymeleafspring.html
      - type: GitHub
        url: https://github.com/thymeleaf/thymeleaf-spring
      - type: Maven Spring6
        url: https://mvnrepository.com/artifact/org.thymeleaf/thymeleaf-spring6
      - type: Maven Spring Boot Starter
        url: https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-thymeleaf
      - type: Spring Security Extras
        url: https://github.com/thymeleaf/thymeleaf-extras-springsecurity
  - aid: thymeleaf:thymeleaf-extras
    name: Thymeleaf Extras and Dialects
    description: Additional Thymeleaf dialect extensions including the Java 8 Time dialect for date/time formatting, the Spring Security dialect for security tag support, and community-maintained dialects such as the Layout Dialect for page-level layout management.
    humanURL: https://www.thymeleaf.org/
    tags:
      - Dialects
      - Extensions
      - Java
      - Template Engine
      - Thymeleaf
    properties:
      - type: GitHub Java8 Time Extras
        url: https://github.com/thymeleaf/thymeleaf-extras-java8time
      - type: GitHub Spring Security Extras
        url: https://github.com/thymeleaf/thymeleaf-extras-springsecurity
      - type: Layout Dialect
        url: https://ultraq.github.io/thymeleaf-layout-dialect/
common:
  - type: Website
    url: https://www.thymeleaf.org/
  - type: Documentation
    url: https://www.thymeleaf.org/doc/tutorials/3.1/usingthymeleaf.html
  - type: GitHub Organization
    url: https://github.com/thymeleaf
  - type: Maven
    url: https://mvnrepository.com/artifact/org.thymeleaf/thymeleaf
  - type: Issue Tracker
    url: https://github.com/thymeleaf/thymeleaf/issues
  - type: Spring Boot Starter
    url: https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-thymeleaf
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/thymeleaf/refs/heads/main/json-schema/thymeleaf-template-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/thymeleaf/refs/heads/main/json-structure/thymeleaf-template-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/thymeleaf/refs/heads/main/json-ld/thymeleaf-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/thymeleaf/refs/heads/main/vocabulary/thymeleaf-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
