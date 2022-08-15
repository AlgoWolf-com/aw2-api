ARG FUNCTION_DIR=user_api/http_api

FROM public.ecr.aws/lambda/python:3.9 AS build-image

RUN pip3 install --upgrade pip wheel

ARG FUNCTION_DIR

COPY ${FUNCTION_DIR}/requirements.txt /build-image/
COPY shared/ /build-image/shared/

RUN pip3 install -r /build-image/requirements.txt \
       --disable-pip-version-check \
       --target "${LAMBDA_TASK_ROOT}"
RUN pip3 install /build-image/shared \
       --disable-pip-version-check \
       --no-cache-dir \
       --target "${LAMBDA_TASK_ROOT}"

FROM public.ecr.aws/lambda/python:3.9 as base-image

COPY --from=build-image ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}

FROM base-image

ARG FUNCTION_DIR

# Copy function code
COPY ${FUNCTION_DIR}/ ${LAMBDA_TASK_ROOT}/

RUN chmod 755 /var/task/schema.json; exit 0

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "function.handler" ]
