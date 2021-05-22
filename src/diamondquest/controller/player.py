"""
PlayerController [DiamondQuest]

Controller for Player.

Author(s): Harley Davis, Jason C. McDonald, Stanislav Schmidt
"""

# LICENSE (BSD-3-Clause)
# Copyright (c) 2020 MousePaw Media.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
#
# CONTRIBUTING
# See https://www.mousepawmedia.com/developers for information
# on how to contribute to our projects.

import logging

import pygame.locals as KEYS

from diamondquest.controller import KeyboardController
from diamondquest.model.game import GameModel
from diamondquest.model.player import PlayerModel
from diamondquest.common import ModeType, Direction
from diamondquest.view.window import Window


logger = logging.getLogger(__name__)


class PlayerController:
    @staticmethod
    def process_action():
        if GameModel.mode == ModeType.MAP:
            if KeyboardController.pending():
                action = KeyboardController.grab()

                player = PlayerModel.get_player()
                # Open Menu
                if action == KEYS.K_ESCAPE:
                    GameModel.mode = ModeType.MENU
                    Window.show_view(ModeType.MENU)

                # Open Journal
                elif action == KEYS.K_j:
                    GameModel.mode = ModeType.JOURNAL
                    Window.show_view(ModeType.JOURNAL)

				# Select Tools (Hand, Pickaxe, Pickaxe, Drill, TNT)
				elif action == KEYS.K_SPACE:
					logger.debug(
                        "PlayerController: process_action - Switch tool to hand"
                    )
					player.select_tool(ToolType.HAND)
				
				elif action == KEYS.K_p:
					logger.debug(
                        "PlayerController: process_action - Switch tool to Pickaxe"
                    )
					player.select_tool(ToolType.PICKAXE)
				
				elif action == KEYS.K_a:
					logger.debug(
                        "PlayerController: process_action - Switch tool to Pickaxe"
                    )
					player.select_tool(ToolType.PICKAXE)

				elif action == KEYS.K_d:
					logger.debug(
                        "PlayerController: process_action - Switch tool to drill"
                    )
					player.select_tool(ToolType.DRILL)
				
				elif action == KEYS.K_t:
					logger.debug(
                        "PlayerController: process_action - Switch tool to TNT"
                    )
					player.select_tool(ToolType.TNT)

                # Handling arrows here
                # They are put back in front in case arrows are held down
                elif action == KEYS.K_UP:
                    logger.debug(
                        "PlayerController: process_action - Trying to move up"
                    )
                    logger.debug(f"Can I move up? - {player.move(Direction.ABOVE)}")
                    logger.debug(
                        "New coords: col, row - "
                        f"{player._location.col}"
                        f"{player._location.row}"
                    )
                elif action == KEYS.K_DOWN:
                    logger.debug(
                        "PlayerController: process_action - Trying to move down"
                    )
                    logger.debug(f"Can I move down? - {player.move(Direction.BELOW)}")
                    logger.debug(
                        "New coords: col, row - "
                        f"{player._location.col}"
                        f"{player._location.row}"
                    )
                elif action == KEYS.K_LEFT:
                    logger.debug(
                        "PlayerController: process_action - Trying to move left"
                    )
                    logger.debug(f"Can I move left? - {player.move(Direction.LEFT)}")
                    logger.debug(
                        "New coords: col, row - "
                        f"{player._location.col}"
                        f"{player._location.row}"
                    )
                elif action == KEYS.K_RIGHT:
                    logger.debug(
                        "PlayerController: process_action - Trying to move right"
                    )
                    logger.debug(f"Can I move right? - {player.move(Direction.RIGHT)}")
                    logger.debug(
                        "New coords: col, row - "
                        f"{player._location.col}"
                        f"{player._location.row}"
                    )
