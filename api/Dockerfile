FROM php:8.3.3-fpm-alpine3.19
ARG APP_DEBUG=false
RUN apk add --no-cache bash git curl zip unzip \
    && if [ "$APP_DEBUG" = "true" ]; then \
      apk add --no-cache $PHPIZE_DEPS \
      && pecl install xdebug \
      && docker-php-ext-enable xdebug \
      && apk del $PHPIZE_DEPS; \
    fi
RUN docker-php-ext-install pdo pdo_mysql
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
