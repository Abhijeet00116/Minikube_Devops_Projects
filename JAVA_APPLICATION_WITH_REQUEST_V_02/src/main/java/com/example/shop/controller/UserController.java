package com.example.shop.controller;

import com.example.shop.model.User;
import com.example.shop.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/users")
public class UserController {

  @Autowired
  private UserRepository userRepository;

  @PostMapping
  public User create(@RequestBody User user) {
    return userRepository.save(user);
  }
}
