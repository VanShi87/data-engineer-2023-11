{% set payment_methods = ['credit_card', 'gift_card', 'coupon', 'bank_transfer'] %}

with orders as (
    select * from {{ref('stg_orders')}}
),

payments as (
         select * from {{ref('stg_payments')}}
),

order_payments as (
    select
        order_id,
        {% for payment_method in payment_methods -%}
            sum(case when payment_method = '{{payment_method}}' then amount else 0 end) as {{payment_method}}_amount,
        {% endfor -%}
        sum(amount) as total_amount
    from payments
    group by order_id
)

select * from order_payments
