# build stage

FROM golang:1.20-alpine AS builder

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -o /fizzbuzz

# run binary

FROM gcr.io/distroless/static-debian11

WORKDIR /

COPY --from=builder /app/templates /templates

COPY --from=builder /fizzbuzz /fizzbuzz

CMD ["./fizzbuzz", "serve"]