import pygame
import numpy as np
import os

white = (255, 255, 255)
black = (0, 0, 0)


class SIF:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def create_funcs(self):
        T = []
        for c in self.coeffs:
            t = np.array(c[:4]).reshape(2, 2)
            h = np.array(c[4:])
            T.append((t, h))

        return T

    def create_attractor(self, surf_e, n_iter):
        size = surf_e.get_size()
        T = self.create_funcs()

        surf_res = pygame.Surface(size)
        surf_iter = pygame.Surface(size)

        surf_res.blit(surf_e, (0, 0))

        size_np = np.array(size)
        for n in range(n_iter):
            surf_iter.fill(white)
            for t in T:
                size_scale = np.int32(np.round(t[0] @ size_np))
                offset = np.int32(np.round(t[1] * size_np))
                s = pygame.transform.smoothscale(surf_res, size_scale)
                surf_iter.blit(s, offset)

            surf_res.blit(surf_iter, (0, 0))

        return surf_res
