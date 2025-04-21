FROM php:8.3.3-fpm-alpine3.19

ARG APP_DEBUG=false

RUN apk add --no-cache bash git curl zip unzip sqlite-dev

RUN if [ "$APP_DEBUG" = "true" ]; then \
        apk add --no-cache $PHPIZE_DEPS linux-headers \
        && pecl install xdebug \
        && rm -f /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
        && cp /usr/local/etc/php/conf.d/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini.bak || true \
        && apk del $PHPIZE_DEPS linux-headers; \
    fi

RUN docker-php-ext-install pdo pdo_sqlite

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

COPY --from=conf /custom.ini /usr/local/etc/php/conf.d/custom.ini
COPY --from=conf /xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini

COPY ./composer.json ./composer.lock ./

COPY . .

RUN if [ "$APP_DEBUG" = "true" ]; then \
    composer install; \
  else \
    composer install --no-dev --optimize-autoloader; \
  fi
