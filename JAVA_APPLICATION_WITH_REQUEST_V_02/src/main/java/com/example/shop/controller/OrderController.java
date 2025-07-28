package com.example.shop.controller;

import com.example.shop.model.Order;
import com.example.shop.repository.OrderRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {

  @Autowired
  private OrderRepository orderRepository;

  @PostMapping
  public Order create(@RequestBody Order order) {
    return orderRepository.save(order);
  }
}
